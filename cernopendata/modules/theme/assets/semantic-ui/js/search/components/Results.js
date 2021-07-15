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
import { Grid, Segment } from "semantic-ui-react";
import {
  Pagination,
  ResultsList,
  ResultsPerPage,
} from "react-searchkit";

const Results = ({
    paginationOptions,
    currentResultsState,
  }) => {
    const { total } = currentResultsState.data;
    return (
      total && (
        <Grid>
          <Grid.Row>
            <Grid.Column width={16}>
              <Segment>
                <Grid>
                  <Grid.Row>
                    <Grid.Column>
                      <ResultsList />
                    </Grid.Column>
                  </Grid.Row>
                </Grid>
              </Segment>
            </Grid.Column>
          </Grid.Row>
          <Grid.Row verticalAlign="middle">
            <Grid.Column width={4}></Grid.Column>              
            <Grid.Column width={8} textAlign="center">
              {total < paginationOptions.resultsPerPage &&
              <Pagination
                options={{
                  size: "mini",
                  showFirst: false,
                  showLast: false,
                }}
              />}
            </Grid.Column>
            <Grid.Column textAlign="right" width={4}>
              <ResultsPerPage
                values={paginationOptions.resultsPerPage}
                label={(cmp) => <> {cmp} results per page</>}
              />
            </Grid.Column>
          </Grid.Row>
        </Grid>
      )
    );
  };

export default Results;
