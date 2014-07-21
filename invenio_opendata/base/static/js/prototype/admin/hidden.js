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
        _ = require("underscore"),
        React = require("react"),
        BoxList = require("jsx!./boxlist"),
        Boxes = {
            Box: require("jsx!../boxes/text"),
            PictureBox: require("jsx!../boxes/picture")
        }

    module.exports = React.createClass({
        getInitialState: function() {
            return {
                "box": null
            }
        },
        onEnable: function(event) {
            var target = $(event.target).closest("a")
            if (target.length) {
                if (this.state.box === target.data("id")) {
                    this.setState({"box": null})
                    this.props.onEnable(target.data("id"))
                } else {
                    this.setState({"box": target.data("id")})
                }
            } else {
                this.setState({"box": null})
            }
            return false
        },
        onDisable: function(event) {
            var id = event.dataTransfer.getData("text")
            this.setState({"box": id})
            this.props.onDisable(id)

            event.preventDefault()
        },
        onDragOver: function(event) {
            event.preventDefault()
        },
        // Swap acts as disabling here as it's put on the trashbin.
        onSwap: function(a, b) {
            this.setState({"box": b})
            this.props.onDisable(b)
        },
        render: function() {
            var boxList = <p>All the boxes are enabled.</p>,
                box = <article onDragOver={this.onDragOver} onDrop={this.onDisable} className="box box-drop">
                        <p>
                            <i className="glyphicon glyphicon-trash"></i><br/>
                            drop here to disable
                        </p>
                    </article>,
                disabled = this.props.collection.disabled(),
                found = false

            if (disabled.length) {
                boxList = <BoxList boxes={disabled}
                                         current={this.state.box}/>
            }

            found = _.inject(disabled, _.bind(function(found, box) {
                return found || (box.get("id") == this.state.box)
            }, this), found)

            if (this.state.box && found) {
                var b = this.props.collection.findWhere({id: this.state.box})
                box = Boxes[b.get("box")](_.extend({onSwap: this.onSwap},
                                                   b.get("data")))
            }

            return (
                <div className={this.props.className} id={this.props.id}>
                    <div className="col-sm-8" onClick={this.onEnable}>
                        <h4>Disabled collections</h4>
                    </div>
                    <div className="col-sm-4" onClick={this.onEnable}>
                        {boxList}
                    </div>
                    <div className="col-sm-4">
                        {box}
                    </div>
                </div>
            )
        }
    })
})
