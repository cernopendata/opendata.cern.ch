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

// AMD format
// ----------
// define(
//     ["jquery",
//      "react",
//      "jsx!prototype/prototype",
//      "json!prototype/data.json"],
//     function($, React, proto, boxes)
// {
//
// CommonJS-like format
// --------------------
define(function(require, exports, module) {
    "use strict";

    var $ = require("jquery"),
        React = require("react"),
        Main = require("jsx!./prototype/main"),
        Backbone = require("backbone"),
        Box = require("./prototype/models/box"),
        Preferences = require("./prototype/models/preferences"),
        BoxesCollection = require("./prototype/collections/boxes"),
        PreferencesCollection = require("./prototype/collections/preferences")

    // Shall be done before any rendering.
    //React.initializeTouchEvents(true)

    var collection = new BoxesCollection(),
        prefsColl = new PreferencesCollection(),
        preferences

    // Reading from local storage
    collection.fetch()
    prefsColl.fetch()

    function bootstrapBoxes() {
        collection.reset()
        // for some reason json! fails here
        //require("json!./prototype/data.json").forEach(function(box, i) {
        JSON.parse(require("text!./prototype/data.json")).forEach(function(box, i) {
            box.position = i
            box.id = "b" + i
            box.data.id = "b" + i
            var b = new Box(box)
            collection.add(b)
            b.save()
        })
    }

    function bootstrapPreferences() {
        preferences = new Preferences()
        prefsColl.reset()
        prefsColl.add(preferences)
        preferences.save()
    }

    if (!collection.length) {
        bootstrapBoxes()
    }

    if (!prefsColl.length) {
        bootstrapPreferences()
    } else {
        preferences = prefsColl.at(0)
    }

    var original = $("div.websearch").before("<div id=__proto__></div>"),
        where = $("#__proto__")[0]

    var current;
    function setView(view) {
        if (current) {
            React.unmountComponentAtNode(where)
        }
        current = view
        React.renderComponent(view, where)
    }

    var main = Main({
        labels: {
            on: "Switch to all the collections",
            off: "Switch to your personal collections",
            visit: "Visit: ",
            moveUp: "Move Up",
            moveDown: "Move Down",
            pushpin: "Pin",
            remove: "Disable"
        },
        preferences: preferences,
        collection: collection,
        onToggle: function(event) {
            original.toggle()
        }
    })

    var Router = Backbone.Router.extend({
        initialize: function() {
            Backbone.history.start()
        },
        routes: {
            '': 'index',
        },
        index: function() {
            setView(main)
        }
    })

    var router = new Router()

    // Easter-egg
    $(".cern-logo a").on("click", function() {
        localStorage.clear()
    })

    module.exports = {
        original: original[0],
        router: router
    }
})
