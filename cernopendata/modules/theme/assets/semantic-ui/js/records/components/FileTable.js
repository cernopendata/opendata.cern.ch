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
import PropTypes from "prop-types";
import { Button, Icon, Table } from "semantic-ui-react";

import { toHumanReadableSize } from "../utils";

const FileTable = ({ items, pidValue }) => {
  return (
    <Table singleLine>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Filename</Table.HeaderCell>
          <Table.HeaderCell>Size</Table.HeaderCell>
          <Table.HeaderCell></Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        {items.files.map((file) => (
          <Table.Row key={file.version_id}>
            <Table.Cell>{file.key}</Table.Cell>
            <Table.Cell collapsing>{toHumanReadableSize(file.size)}</Table.Cell>
            <Table.Cell collapsing>
              {file.type === "index.txt" && (
                <Button icon size="mini">
                  <Icon name="list" /> List files
                </Button>
              )}
              <Button
                as="a"
                icon
                size="mini"
                primary
                href={`/record/${pidValue}/files/${file.key}`}
              >
                <Icon name="download" /> Download
              </Button>
            </Table.Cell>
          </Table.Row>
        ))}
      </Table.Body>
    </Table>
  );
};

export default FileTable;

FileTable.propTypes = {
  items: PropTypes.object.isRequired,
  pidValue: PropTypes.string.isRequired,
};
