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
        React = require("react"),
        Configuration = require("jsx!./configuration"),
        Hidden = require("jsx!./hidden"),
        Search = require("jsx!./search")

    module.exports = React.createClass({
        onCancel: function() {
            console.log("cancel")
            this.onClose()
        },
        onSave: function() {
            console.log("save and close")
            this.onClose()
        },
        onClose: function() {
            this.props.setState({admin: false})
        },
        onTabClick: function(event) {
            var target = $(event.target).closest("a")
            if (target.length) {
                var tab = parseInt(target.attr("href").slice(-1), 10)
                this.props.setState({tab: tab})
            }
            return false
        },
        render: function() {
            var style = {display: this.props.personal && this.props.admin ? "block": "none"},
                boxes = this.props.preferences.get("boxes"),
                hide = {"display": "block"},
                tab1 = "tab-pane",
                item1, item2, item3,
                tab2 = tab1,
                tab3 = tab2,
                active = "active"

            switch (this.props.tab) {
                case 1:
                    tab1 += " " + active
                    item1 = active
                    break
                case 2:
                    tab2 += " " + active
                    item2 = active
                    break
                case 3:
                    tab3 += " " + active
                    item3 = active
                    break
            }

            return (
                <div className="prototype-admin form-horizontal" style={style}>
                    <div className="row">
                        <div className="col-sm-4">
                            <ul className="nav nav-pills nav-stacked" role="tablist" onClick={this.onTabClick}>
                                <li className={item1}><a href="#prototype-admin-tab1">Find more collections</a></li>
                                <li className={item2}><a href="#prototype-admin-tab2">Disabled collections</a></li>
                                <li className={item3}><a href="#prototype-admin-tab3">Settings</a></li>
                            </ul>
                        </div>
                        <div className="tab-content">
                            <Search className={tab1}
                                    id="prototype-admin-tab1"
                                    collection={this.props.collection}
                                    onEnable={this.props.onEnable}/>
                            <Hidden className={tab2}
                                    id="prototype-admin-tab2"
                                    collection={this.props.collection}
                                    onEnable={this.props.onEnable}
                                    onDisable={this.props.onDisable}/>
                            <Configuration className={tab3}
                                           id="prototype-admin-tab3"
                                           boxes={boxes}
                                           onVisibleBoxes={this.props.onVisibleBoxes}/>
                        </div>
                    </div>
                </div>
            )
        }
    })
})
