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

    var React = require('react')

    var Switch = React.createClass({
        handleClick: function() {
            this.props.onPersonal(!this.props.personal)
            return false
        },
        render: function() {
            var label = this.props.personal ?
                this.props.labels.on :
                this.props.labels.off

            return (
                <p className={this.props.className}>
                    <a href="#" onClick={this.handleClick}>{label}</a>
                </p>
            )
        }
    })

    var Hamburger = React.createClass({
        handleClick: function() {
            this.props.onAdmin(!this.props.admin)
            return false
        },
        render: function() {
            var className = this.props.className + " hamburger text-right"
            var style = {};
            if (!this.props.personal) {
                style.display = "none"
            }
            return (
                <p className={className} style={style}>
                    <a href="#" onClick={this.handleClick}>
                        <i className="fa fa-pencil"></i>{' '}edit
                    </a>
                </p>
            )
        }
    })

    module.exports = React.createClass({
        onAdmin: function(admin) {
            this.props.setState({admin: admin})
        },
        onPersonal: function(personal) {
            this.props.setState({personal: personal})
        },
        render: function() {
            var className = "col-md-6"
            return (
                <div className="row">
                    <Switch className={className}
                            labels={this.props.labels}
                            personal={this.props.personal}
                            onPersonal={this.onPersonal} />
                    <Hamburger className={className}
                               admin={this.props.admin}
                               personal={this.props.personal}
                               onAdmin={this.onAdmin}/>
                </div>
            )
        }
    })
})
