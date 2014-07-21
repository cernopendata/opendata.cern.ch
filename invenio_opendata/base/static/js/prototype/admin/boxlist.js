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

    var React = require("react"),
        $ = require("jquery"),
        _ = require("underscore")

    module.exports = React.createClass({
        onDragStart: function(event) {
            event.dataTransfer.setData("text", $(event.target).data("id"))
        },
        render: function() {
            return (
                <ul className="nav nav-stacked">
                    {this.props.boxes.map(_.bind(function(box){
                        var data = box.get("data"),
                            glyphicon = "",
                            className = ""

                        if (box.get("id") == this.props.current) {
                            className = "active"
                            glyphicon = <span className="pull-right">
                                    <i className="glyphicon glyphicon-plus"></i>
                                </span>
                        }

                        return (
                            <li key={box.get("id")} className={className}
                                draggable="true" onDragStart={this.onDragStart}>
                                <a href={data.header.href} data-id={box.get("id")}>
                                    {glyphicon}{' '}{data.header.title}
                                </a>
                            </li>
                        )
                    }, this))}
                </ul>
            )
        }
    })
})
