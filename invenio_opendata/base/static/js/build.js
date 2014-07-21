/*
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

({
    baseUrl: '',
    preserveLicenseComments: false,
    optimize: 'uglify2',
    uglify2: {
        output: {
            beautify: false,
            comments: false
        },
        compress: {
            drop_console: true
        },
        warnings: true,
        mangle: false
    },
    paths: {
        jquery: 'empty:',
        'jquery.form': 'empty:',
        react: 'vendors/jsx-requirejs-plugin/js/react-with-addons-0.10.0',
        jsx: 'vendors/jsx-requirejs-plugin/js/jsx',
        JSXTransformer: 'vendors/jsx-requirejs-plugin/js/JSXTransformer-0.10.0',
        text: 'vendors/requirejs-plugins/lib/text',
        json: 'vendors/requirejs-plugins/src/json',
        backbone: 'vendors/backbone/backbone',
        'backbone.localStorage': 'vendors/backbone.localstorage/backbone.localStorage',
        underscore: 'vendors/underscore/underscore',
        typeahead: 'js/typeahead',
        prototype: 'js/prototype',
        app: 'js/app',
    },
    shim: {
        react: { exports: 'React' },
        jquery: { exports: '$' },
        backbone: { deps: ['underscore', 'jquery'], exports: 'Backbone'},
        'backbone.localstorage': { deps: ['backbone'], exports: 'Backbone.LocalStorage' },
        underscore: { exports: '_' }
    },
    onBuildWrite: function (moduleName, path, singleContents) {
        // Dropping jsx related files
        if (['jsx', 'JSXTransformer'].indexOf(moduleName) >= 0) {
            return '';
        }
        return singleContents.replace(/jsx!/g, '');
    }
})
