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

    var React = require('react'),
        AdminBar = require("jsx!./admin/main"),
        TopBar = require("jsx!./topbar"),
        Grid = require("jsx!./grid"),
        _ = require("underscore")

    module.exports = React.createClass({
        getInitialState: function() {
            var state = {
                personal: this.props.preferences.get("personal"),
                admin: this.props.preferences.get("admin"),
                length: this.props.preferences.get("boxes"),
                tab: this.props.preferences.get("tab")
            }

            if (state.personal) {
                this.props.onToggle()
            }

            return state
        },
        onState: function(state) {
            if ("personal" in state && state.personal != this.state.personal) {
                this.props.onToggle()
            }
            this.props.preferences.set(state)
            this.props.preferences.save()
            this.setState(state)
        },
        // DEPRECATED! Use onShuffle
        // a is null, means b moves up
        // b is null, means a moves down
        onSwap: function(a, b) {
            var collection = this.props.collection,
                boxA, boxB, position

            if (!b && !a) {
                boxB = collection.findWhere({id: b})
            }
            if (a) {
                boxA = collection.findWhere({id: a})
                if (!b) {
                    position = collection.indexOf(boxA)
                    do {
                        position += 1
                        boxB = collection.at(position)
                    } while(boxB !== undefined && boxB.get("disabled"))
                    if (!boxB) {
                        return // no changes
                    }
                } else {
                    boxB = collection.findWhere({id: b})
                }
            } else {
                boxB = collection.findWhere({id: b})

                position = collection.indexOf(boxB)
                do {
                    position -= 1
                    boxA = collection.at(position)
                } while(boxA !== undefined && boxA.get("disabled"))
                if (!boxA) {
                    return  // no changes
                }
            }

            position = boxA.get("position")

            if (!boxB.get("disabled") && !boxB.get("searchable")) {
                boxA.set("position", boxB.get("position"))
                boxB.set("position", position)
            } else {
                // update all the position!!
                collection.each(function(box) {
                    if (box.get("position") > boxA.get("position")) {
                        box.set("position", box.get("position") + 1)
                    }
                })
                boxB.set("position", boxA.get("position"))
                boxB.set("disabled", false)
                boxA.set("position", boxA.get("position") + 1)
            }

            boxA.save()
            boxB.save()
            collection.sort()
            this.setProps({collection: collection})
        },
        // a: target, b: source
        onShuffle: function(a, b) {
            console.log(b + " -> " + a)
            var collection = this.props.collection,
                boxA, boxB, position

            if (!b && !a) {
                boxB = collection.findWhere({id: b})
            }
            if (a) {
                boxA = collection.findWhere({id: a})
                if (!b) {
                    position = collection.indexOf(boxA)
                    do {
                        position += 1
                        boxB = collection.at(position)
                    } while(boxB !== undefined && boxB.get("disabled"))
                    if (!boxB) {
                        return // no changes
                    }
                } else {
                    boxB = collection.findWhere({id: b})
                }
            } else {
                boxB = collection.findWhere({id: b})

                position = collection.indexOf(boxB)
                do {
                    position -= 1
                    boxA = collection.at(position)
                } while(boxA !== undefined && boxA.get("disabled"))
                if (!boxA) {
                    return  // no changes
                }
            }

            if (!boxB.get("disabled") && !boxB.get("searchable")) {
                var posA = parseInt(boxA.get("position"), 10),
                    posB = parseInt(boxB.get("position"), 10)

                // B goes towards A that is before in the list
                if (posA < posB) {
                    collection.each(function(box) {
                        position = parseInt(box.get("position"), 10)
                        if (position >= posA && position < posB) {
                            box.set("position", position + 1)
                            box.save()
                        }
                    })
                    boxB.set("position", posA)
                    boxB.save()
                // B goes towards A that is after in the list
                } else {
                    collection.each(function(box) {
                        position = parseInt(box.get("position"), 10)
                        if (position > posB && position <= posA) {
                            box.set("position", position - 1)
                            box.save()
                        }
                    })
                    boxB.set("position", posA)
                    boxB.save()
                }
            } else {
                // update all the position!!
                collection.each(function(box) {
                    if (box.get("position") > boxA.get("position")) {
                        box.set("position", box.get("position") + 1)
                        box.save()
                    }
                })
                boxB.set("position", boxA.get("position"))
                boxB.set("disabled", false)
                boxB.set("searchable", false)
                boxA.set("position", boxA.get("position") + 1)
                boxA.save()
                boxB.save()
            }

            collection.sort()
            this.setProps({collection: collection})
        },
        onEnable: function(a) {
            var collection = this.props.collection,
                boxA = collection.findWhere({id: a}),
                minPosition = collection.at(0).get("position")

            boxA.set("disabled", false)
            boxA.set("searchable", false)
            boxA.set("position", minPosition - 1)
            boxA.save()
            collection.sort()
            this.setProps({collection: collection})
        },
        onDisable: function(a) {
            var collection = this.props.collection,
                boxA = collection.findWhere({id: a})

            boxA.set("disabled", true)
            boxA.save()
            this.setProps({collection: collection})
        },
        onVisibleBoxes: function(boxes) {
            var preferences = this.props.preferences
            console.log(boxes)
            preferences.set("boxes", boxes)
            preferences.save()
            this.setState({length: boxes})
            this.setProps({preferences: preferences})
        },
        render: function() {
            var boxes = this.props.collection.enabled().map(_.bind(function(box) {
                box.set("data", _.extend({labels: this.props.labels},
                                         box.get("data")))
                return box
            }, this))

            return (
                <div>
                    <TopBar labels={this.props.labels}
                            personal={this.state.personal}
                            admin={this.state.admin}
                            setState={this.onState}/>
                    <AdminBar collection={this.props.collection}
                              preferences={this.props.preferences}
                              onVisibleBoxes={this.onVisibleBoxes}
                              personal={this.state.personal}
                              admin={this.state.admin}
                              tab={this.state.tab}
                              setState={this.onState}
                              onEnable={this.onEnable}
                              onDisable={this.onDisable}/>
                    <Grid boxes={boxes}
                          length={this.state.length}
                          plus={this.state.plus}
                          personal={this.state.personal}
                          admin={this.state.admin}
                          onSwap={this.onShuffle}
                          onDisable={this.onDisable}
                          onPlus={this.onPlus}/>
                </div>
            )
        }
    })
})
