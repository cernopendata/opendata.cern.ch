#!/usr/bin/env python

"""Utility to fetch facet hierarchy."""

import pprint

import requests


def main():
    """Main script doing the work."""
    facet_hierarchy = dict()
    response = requests.get("http://opendata.cern.ch/api/records")
    aggs = response.json().get("aggregations")
    for agg, agg_v in aggs.items():
        facet_hierarchy[agg] = dict()
        for bucket in agg_v["buckets"]:
            facet_hierarchy[agg][bucket["key"]] = dict()
            subfacet_hierarchy = facet_hierarchy[agg][bucket["key"]]
            if f"sub{agg}" in bucket:
                subfacet_hierarchy[f"sub{agg}"] = set()
                for subagg in bucket[f"sub{agg}"]["buckets"]:
                    subfacet_hierarchy[f"sub{agg}"].add(subagg["key"])

    pprint.pprint(facet_hierarchy)


if __name__ == "__main__":
    main()
