/*
 * -*- coding: utf-8 -*-
 *
 * This file is part of CERN Open Data Portal.
 * Copyright (C) 2021, 2023 CERN.
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

/**
 * Converts size in bytes to human readable expression.
 * @param {number} bytes - Bytes to convert
 * @param {number} [precision=1] - Number of decimals
 */
export function toHumanReadableSize(bytes, precision = 1) {
  if (isNaN(parseFloat(bytes)) || !isFinite(bytes)) {
    return "-";
  }
  const units = ["bytes", "KiB", "MiB", "GiB", "TiB", "PiB"];
  const number = Math.floor(Math.log(bytes) / Math.log(1024));
  return `${(bytes / Math.pow(1024, number)).toFixed(precision)} ${
    units[number]
  }`;
}
