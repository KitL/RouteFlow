/* Copyright 2008 (C) Nicira, Inc.
 *
 * This file is part of NOX.
 *
 * NOX is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NOX is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NOX.  If not, see <http://www.gnu.org/licenses/>.
 */
%module "nox.netapps.storage"

%{
#include "pystorage.cc"
%}

class PyStorage {
public:
    PyStorage(PyObject*);
    void configure(PyObject*);
    void install(PyObject*);
    PyObject* create_table(PyObject*, PyObject*, PyObject*, PyObject*);
    PyObject* drop_table(PyObject*, PyObject*);
    PyObject* get(PyObject*, PyObject*, PyObject*);
    PyObject* get_next(PyObject*, PyObject*);
    PyObject* put(PyObject*, PyObject*, PyObject*);
    PyObject* modify(PyObject*, PyObject*, PyObject*);
    PyObject* remove(PyObject*, PyObject*);
    PyObject* put_row_trigger(PyObject*, PyObject*, PyObject*);
    PyObject* put_table_trigger(PyObject*, PyObject*, PyObject*, PyObject*);
    PyObject* remove_trigger(PyObject*, PyObject*);
};

