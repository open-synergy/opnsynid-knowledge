# -*- coding: utf-8 -*-
# Copyright 2014 Savoir-faire Linux
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Document Management System for Multiple Records",
    "version": "8.0.2.0.0",
    "category": "Knowledge Management",
    "summary": "Document Management System for Multiple Records",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA), "
    "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "license": "AGPL-3",
    "depends": [
        "document",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/document_wizard_view.xml",
        "views/ir_attachment_view.xml",
        "attachment_multiple_record.xml",
    ],
    "qweb": ["static/src/xml/document.xml"],
    "test": [],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "post_init_hook": "update_existing_attachment",
}
