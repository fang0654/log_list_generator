#!/usr/bin/env python3

import argparse
import os
import datetime
import pdb
import glob


def get_def_filename():

    return os.path.join(os.path.dirname(__file__), "log_names.tmpl")


parser = argparse.ArgumentParser()

parser.add_argument(
    "-t",
    "--template",
    help="Template folder containing .tmpl files to use (default templates)",
    default=os.path.join(os.path.dirname(__file__), "templates"),
)

parser.add_argument(
    "-o",
    "--output",
    help="Output file for generated wordlist. (default lognames.txt)",
    default="lognames.txt",
)

parser.add_argument(
    "-d",
    "--days",
    help="Number of days back to generate (default 14)",
    type=int,
    default=14,
)

parser.add_argument(
    "-p", "--pid", help="Max PID (default 10000)", type=int, default=10000
)

parser.add_argument(
    "--it",
    help="Ignore time formatting - vastly reduces the number of possibilities",
    action="store_true",
)
opts = parser.parse_args()

today = datetime.date.today()
dates = []

for i in range(opts.days):
    d = today - datetime.timedelta(days=i)
    dates.append(
        {
            "d": d.strftime("%d"),
            "m": d.strftime("%m"),
            "y": d.strftime("%y"),
            "Y": d.strftime("%Y"),
            "W": d.strftime("%W"),
        }
    )

with open(opts.output, "w") as o:

    for tmpl in glob.glob(f"{opts.template}/*.tmpl"):
        with open(tmpl, "r") as tpl_file:
            for t in tpl_file:
                if t[-1] != "\n":
                    t += "\n"
                if t and len(t) > 1 and t[0] != "#":
                    if (
                        "{d}" in t
                        or "{m}" in t
                        or "{y}" in t
                        or "{Y}" in t
                        or "{W}" in t
                    ):
                        for d in dates:
                            if "{h}" in t or "{M}" in t or "{s}" in t:

                                if "{h}" in t and not opts.it:
                                    for h in range(24):
                                        d["h"] = h
                                        if "{M}" in t:
                                            for M in range(60):
                                                d["M"] = M
                                                if "{s}" in t:
                                                    for s in range(60):
                                                        d["s"] = s
                                                        o.write(t.format(**d))
                                                else:
                                                    o.write(t.format(**d))
                                        else:
                                            o.write(t.format(**d))
                            else:
                                o.write(t.format(**d))

                            o.write(t.format(**d))
                    elif "{pid}" in t:
                        for pid in range(opts.pid + 1):
                            o.write(t.format(pid=pid))

                    else:
                        o.write(t)
                        o.write(f"{t[:-1]}.gz\n")
                        o.write(f"{t[:-1]}.1.gz\n")
                        o.write(f"{t[:-1]}.1\n")
