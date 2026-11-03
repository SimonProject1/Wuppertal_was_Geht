import json,datetime,pathlib
p=pathlib.Path("data/events.json"); d=json.loads(p.read_text(encoding="utf-8")); required={"id","title","date","start","venue","category","url","source","status"}; assert isinstance(d.get("events"),list);
for e in d["events"]: assert not (required-set(e)), f"Fehlende Felder: {required-set(e)}"; datetime.date.fromisoformat(e["date"]); assert e["url"].startswith("https://")
print(f"{len(d['events'])} Events gültig")
