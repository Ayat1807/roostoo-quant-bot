"""US macro event calendar: CPI releases, FOMC decisions, FOMC minutes (2020 -> 2026-10).

    python -m lab.events            # rebuild data/events.csv from the official calendars

Sources (official):
  * FOMC decisions and minutes: federalreserve.gov/monetarypolicy/fomccalendars.htm (2021+)
    and fomchistorical2020.htm. Decision day = the statement date (monetaryYYYYMMDDa.htm).
    Notation votes are not policy-rate decisions and are excluded; the 2020 emergency cuts
    (Mar 3, Mar 15) are kept. Minutes = the "(Released ...)" date of each meeting.
  * CPI: bls.gov/bls/news-release/cpi.htm (release archive, file names cpi_MMDDYYYY) and
    bls.gov/schedule/news_release/cpi.htm (upcoming releases). bls.gov refuses scripted
    requests (HTTP 403), so both are read from the Internet Archive's copy of the BLS page.
Times (US Eastern, converted to UTC with DST): CPI 08:30; FOMC statement 14:00 (2020-03-03
10:00, 2020-03-15 17:00); minutes 14:00. Releases after the fetch date are status=scheduled;
minutes of a meeting whose minutes are not out yet are dated 3 weeks after it (the Fed's rule)
and marked scheduled_rule.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd
import requests

OUT = Path(__file__).resolve().parent.parent / "data" / "events.csv"
UA = {"User-Agent": "Mozilla/5.0 (research; strategy_lab event calendar)"}
FED = "https://www.federalreserve.gov/monetarypolicy/"
BLS_ARCHIVE = "https://web.archive.org/web/2026id_/https://www.bls.gov/bls/news-release/cpi.htm"
BLS_SCHED = "https://web.archive.org/web/2026id_/https://www.bls.gov/schedule/news_release/cpi.htm"
START, END = pd.Timestamp("2020-01-01"), pd.Timestamp("2026-10-31")
SPECIAL_ET = {"2020-03-03": "10:00", "2020-03-15": "17:00"}
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct",
                                      "nov", "dec"], 1)}


def get(url: str) -> str:
    r = requests.get(url, headers=UA, timeout=60)
    r.raise_for_status()
    return r.text


def to_utc(day: str, hhmm: str) -> pd.Timestamp:
    return pd.Timestamp(f"{day} {hhmm}").tz_localize("America/New_York").tz_convert("UTC")


def fomc() -> list[dict]:
    rows = []
    for page, sep in (("fomccalendars.htm", r'<div class="[^"]*row fomc-meeting"'), ("fomchistorical2020.htm", r"<h5")):
        t = get(FED + page)
        years = [(m.start(), int(m.group(1))) for m in re.finditer(r"(\d{4}) FOMC Meetings", t)]
        pos = 0
        for blk in re.split(sep, t)[1:]:
            pos = t.find(blk, pos)
            head = re.sub(r"<[^>]+>", " ", blk[:600])
            if re.search(r"notation vote|cancelled", head, re.I):
                continue
            st = re.search(r"monetary(\d{8})a\.htm", blk)
            mon = re.search(r'fomc-meeting__month[^>]*><strong>([A-Za-z]+)(?:/([A-Za-z]+))?</strong>', blk)
            dd = re.search(r'fomc-meeting__date[^>]*>\s*(?:\d+-)?(\d+)', blk)
            if st:
                day = pd.Timestamp(st.group(1))
            elif page == "fomccalendars.htm" and mon and dd and years:
                # upcoming meeting (no statement yet): decision on the last meeting day
                yr = max((y for p, y in years if p < pos), default=None)
                if yr is None:
                    continue
                day = pd.Timestamp(f"{mon.group(2) or mon.group(1)} {dd.group(1)} {yr}")
            else:
                continue
            rows.append({"type": "FOMC_DECISION", "date_et": str(day.date()), "ref": f"FOMC {day:%Y-%m-%d}",
                         "src": FED + page})
            rel = re.search(r"Released ([A-Za-z]+ \d+, \d{4})", blk)
            if rel and pd.Timestamp(rel.group(1)) < day + pd.Timedelta(days=7):
                rel = None        # 2020-03-02 unscheduled meeting: that date is the statement's
            if rel:
                rows.append({"type": "FOMC_MINUTES", "date_et": str(pd.Timestamp(rel.group(1)).date()),
                             "ref": f"minutes of FOMC {day:%Y-%m-%d}", "src": FED + page})
            elif day >= pd.Timestamp("2026-01-01"):
                rows.append({"type": "FOMC_MINUTES", "date_et": str((day + pd.Timedelta(days=21)).date()),
                             "ref": f"minutes of FOMC {day:%Y-%m-%d}", "src": FED + page, "rule": True})
    return rows


def cpi() -> list[dict]:
    rows = []
    t = get(BLS_ARCHIVE)
    for m in re.finditer(r'cpi_(\d{2})(\d{2})(\d{4})\.htm">([A-Za-z]+ \d{4}) Consumer Price Index', t):
        mm, dd, yy, ref = m.groups()
        rows.append({"type": "CPI", "date_et": f"{yy}-{mm}-{dd}", "ref": f"CPI {ref}", "src": BLS_ARCHIVE})
    s = get(BLS_SCHED)
    for ref, mon, d, y in re.findall(r"<td>([A-Z][a-z]+ \d{4})</td>\s*<td>([A-Za-z]{3})[a-z]*\.? (\d{1,2}), (\d{4})</td>", s):
        rows.append({"type": "CPI", "date_et": f"{y}-{MONTHS[mon.lower()]:02d}-{int(d):02d}", "ref": f"CPI {ref}",
                     "src": BLS_SCHED})
    return rows


def build(today: pd.Timestamp | None = None) -> pd.DataFrame:
    today = today or pd.Timestamp.now(tz="UTC")
    df = pd.DataFrame(fomc() + cpi())
    if "rule" not in df:
        df["rule"] = False
    df["rule"] = df["rule"].fillna(False).astype(bool)
    df = df[(pd.to_datetime(df["date_et"]) >= START) & (pd.to_datetime(df["date_et"]) <= END)]
    df = df.sort_values(["date_et", "type", "src"]).drop_duplicates(["type", "date_et"], keep="first")
    et = {"CPI": "08:30", "FOMC_DECISION": "14:00", "FOMC_MINUTES": "14:00"}
    df["time_et"] = [SPECIAL_ET.get(d, et[t]) if t == "FOMC_DECISION" else et[t]
                     for t, d in zip(df["type"], df["date_et"])]
    df["time_utc"] = [to_utc(d, h).strftime("%Y-%m-%dT%H:%MZ") for d, h in zip(df["date_et"], df["time_et"])]
    df["status"] = ["scheduled_rule" if r else ("scheduled" if pd.Timestamp(u) > today else "released")
                    for r, u in zip(df["rule"], df["time_utc"])]
    return df[["time_utc", "type", "date_et", "time_et", "ref", "status", "src"]].reset_index(drop=True)


def load_events(types: tuple[str, ...] = ("CPI", "FOMC_DECISION", "FOMC_MINUTES")) -> pd.DataFrame:
    df = pd.read_csv(OUT)
    df["time"] = pd.to_datetime(df["time_utc"], utc=True)
    return df[df["type"].isin(types)].reset_index(drop=True)


if __name__ == "__main__":
    df = build()
    df.to_csv(OUT, index=False)
    print(df.groupby([df["date_et"].str[:4], "type"]).size().unstack(fill_value=0))
    print(f"{len(df)} events -> {OUT}")
