/** @jsx React.DOM
 *
 * This file is part of Invenio.
 * Copyright (C) 2014 CERN.
 *
 * Invenio is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * Invenio is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Invenio; if not, write to the Free Software Foundation, Inc.,
 * 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
 */

define(function(require, exports, module) {
    "use strict";

    var $ = require("jquery"),
        React = require("react")

    module.exports = React.createClass({
        onRow: function(event) {
            var boxes = parseInt($(event.target).text(), 10)
            this.props.onVisibleBoxes(boxes)
        },
        render: function() {
            var boxes = this.props.boxes

            return (
                <div className={this.props.className} id={this.props.id}>
                    <div className="col-sm-8">
                        <h4>Settings</h4>
                    </div>
                    <div className="col-sm-4">
                        <p className="box-label">Visible boxes by default</p>
                    </div>
                    <div className="col-sm-4">
                        <div className="btn-group" onClick={this.onRow}>
                            {[3,6,9].map(function(row, index) {
                                var classes = "btn",
                                    key = "btn" + index

                                if (row == boxes) {
                                    classes += " btn-primary"
                                } else {
                                    classes += " btn-default"
                                }
                                return (
                                    <button type="button"
                                            className={classes}
                                            key={key}>
                                        {row}
                                    </button>
                                )
                            })}
                        </div>
                    </div>
                </div>
            )
        }
    })
})
