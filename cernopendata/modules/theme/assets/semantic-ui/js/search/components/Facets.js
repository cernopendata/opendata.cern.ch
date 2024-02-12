/*
 * -*- coding: utf-8 -*-
 *
 * This file is part of CERN Open Data Portal.
 * Copyright (C) 2021 CERN.
 *
 * CERN Open Data Portal is free software; you can redistribute it
 * and/or modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * CERN Open Data Portal is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with CERN Open Data Portal; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
 * MA 02111-1307, USA.
 *
 * In applying this license, CERN does not
 * waive the privileges and immunities granted to it by virtue of its status
 * as an Intergovernmental Organization or submit itself to any jurisdiction.
 */

import React from "react";
import { BucketAggregation, Toggle, ActiveFilters, withState } from "react-searchkit";

const CODFacets = ({ aggs, updateQueryState, currentQueryState }) => {
  return (
    <>
      <div class="ui card" visibility="display">
        <div class="content">
          <div class="header">Current parameters
          <tag id="clear_all" class="ui" primary onClick={() => updateQueryState({... currentQueryState, filters:[], })}><a href >Clear all</a></tag>
          </div>
        </div>
        <div class="content"><ActiveFilters /></div>
      </div>

      <Toggle
        title="Availability"
        label="include on-demand datasets"
        filterValue={["ondemand", "ondemand"]}
      />
      {aggs.map((agg) => (
        <BucketAggregation key={agg.title} title={agg.title} agg={agg.agg} />
      ))}
    </>
  );
};

export default withState(CODFacets);
