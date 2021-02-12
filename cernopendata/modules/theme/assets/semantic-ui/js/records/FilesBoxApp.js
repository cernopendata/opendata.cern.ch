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

import React, { useEffect, useState } from "react";
import { Pagination } from "semantic-ui-react";

import { FileTable } from "./components";
import config, { ITEMS_PER_PAGE, RECORD_FILEPAGE_URL } from "./config";

const FilesBoxApp = () => {
  const [page, setPage] = useState(1);
  const [files, setFiles] = useState({});
  const [indexFiles, setIndexFiles] = useState({});
  const { pidValue } = config;

  useEffect(() => {
    const type = getType();
    fetch(RECORD_FILEPAGE_URL(pidValue, page, type))
      .then((response) => response.json())
      .then((data) => {
        if (type === "files") {
          setFiles(data);
        } else if (type === "index_files") {
          setIndexFiles(data);
        } else {
          setFiles(data.files);
          setIndexFiles(data.index_files);
        }
      });
  }, [page]);

  const getType = () => {
    if (files.total) {
      return "files";
    } else if (indexFiles.total) {
      return "index_files";
    }
    return null;
  };

  const handlePaginationChange = (e, { activePage }) => {
    setPage(activePage);
  };

  const renderFileTable = (items, title) => (
    <>
      {items.total > 0 && (
        <>
          <h3>{title}</h3>
          <FileTable items={items} pidValue={pidValue} />
        </>
      )}
      {items.total > ITEMS_PER_PAGE && (
        <Pagination
          activePage={page}
          onPageChange={handlePaginationChange}
          totalPages={Math.ceil(items.total / ITEMS_PER_PAGE)}
        />
      )}
    </>
  );

  return (
    <>
      {renderFileTable(files, "Files")}
      {renderFileTable(indexFiles, "File Indexes")}
    </>
  );
};

export default FilesBoxApp;
