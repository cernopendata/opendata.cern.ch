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

    var $ = require("jquery"),
        _ = require("underscore"),
        React = require("react")

    module.exports = React.createClass({
        onMenu: function(event) {
            this.killEvent(event)
            this.props.onMenu(event)
        },
        onDisable: function(event) {
            this.props.onDisable(this.props.id)
        },
        /*
         * Killing the event if it doesn't come from an anchor.
         */
        killEvent: function(event) {
            var target = $(event.target).closest("a, button")
            if (!target.length) {
                event.stopPropagation()
            }
        },
        componentDidMount: function() {
            // If we click outside the component, then we should hide the
            // admin menu.
            this.handler = _.bind(function(event) {
                var target = $(event.target).closest("*[data-reactid=" + this._rootNodeID + "]")
                if (!target.length) {
                    this.props.onMenu(event)
                }
            }, this)
            $("body").on("click", this.handler)
        },
        componentWillUnmount: function() {
            $("body").off("click", this.handler)
            this.handler = undefined
        },
        render: function() {
            var href = this.props.href || "#",
                title = this.props.title || "Untitled",
                labels = this.props.labels

            /* Not a feature as of yet.
                        <button type="button" className="btn btn-default">
                            <i className="glyphicon glyphicon-pushpin"></i>
                            {' '}{labels.pushpin}
                        </button>
            */
            return (
                <div className="box-admin" onClick={this.onMenu} onTouchStart={this.props.onMenu}>
                    <div className="box-admin-buttons btn-group-vertical" onTouchStart={this.killEvent}>
                        <a href={href} className="btn btn-primary">
                            {labels.visit} “{title}”
                        </a>
                        <button type="button" className="btn btn-default" onClick={this.props.onMoveUp}>
                            <i className="glyphicon glyphicon-arrow-up"></i>
                            {' '}{labels.moveUp}
                        </button>
                        <button type="button" className="btn btn-default" onClick={this.props.onMoveDown}>
                            <i className="glyphicon glyphicon-arrow-down"></i>
                            {' '}{labels.moveDown}
                        </button>
                        <button type="button" className="btn btn-danger" onClick={this.onDisable}>
                            <i className="glyphicon glyphicon-remove"></i>
                            {' '}{labels.remove}
                        </button>
                    </div>
                </div>
            )
        }
    })
})
