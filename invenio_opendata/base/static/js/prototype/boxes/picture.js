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
        React = require("react"),
        Admin = require("jsx!./admin")

    module.exports = React.createClass({
        getInitialState: function() {
            return {edit: false}
        },
        onMenu: function(event) {
            this.setState({edit: !this.state.edit})
            return false
        },
        onMoveUp: function(event) {
            this.props.onSwap(null, this.props.id)
            event.preventDefault()
        },
        onMoveDown: function(event) {
            this.props.onSwap(this.props.id, null)
            event.preventDefault()
        },
        onDragOver: function(event) {
            event.preventDefault();
        },
        onDragStart: function(event) {
            event.dataTransfer.setData("text", this.props.id)
        },
        onDrop: function(event) {
            event.preventDefault();
            this.props.onSwap(this.props.id, event.dataTransfer.getData("text"))
        },
        onDisable: function(box) {
            this.props.onDisable(box)
        },
        render: function() {
            var header = $.extend({"href": "#"}, this.props.header),
                footer = $.extend({"label": "more {header.title}", "href": header.href}, this.props.footer),
                style = {background: "url(" + this.props.backgroundImage + ") 50% 50%",
                         minHeight: "330px"},
                edit = ""

            var className = "box-body";
            if (!("wrap" in this.props) || this.props.wrap) {
                className += " wrap";
            }

            if (this.state.edit) {
                edit = <Admin id={this.props.id}
                              title={header.title}
                              href={header.href}
                              labels={this.props.labels}
                              onMenu={this.onMenu}
                              onMoveUp={this.onMoveUp}
                              onMoveDown={this.onMoveDown}
                              onDisable={this.props.onDisable}/>
            }

            return (
                <article className="box box-picture" style={style}
                         draggable="true" onDragStart={this.onDragStart}
                         onDrop={this.onDrop} onDragOver={this.onDragOver}>
                    <header>
                        <h2>
                            <a href={header.href} onClick={this.onMenu}>
                                {header.title}&nbsp;&nbsp;<i className="glyphicon glyphicon-cog"></i>
                            </a>
                        </h2>
                    </header>
                    <div className={className} dangerouslySetInnerHTML={{__html: this.props.body}}/>
                    <footer>
                        <p>
                            <a href={footer.href}>{footer.label} »</a>
                        </p>
                    </footer>
                    {edit}
                </article>
            )
        }
    })
})
