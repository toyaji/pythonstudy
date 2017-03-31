import json

obj ="""
{"name":'wes',
"places_lived': ["United States", "Spain", "Germany"],
"pet": null,
"siblings":[{"name": "Scott", "age": 25, "pet": "Zuko"},
{"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""

result = json.loads(obj)
print(result)