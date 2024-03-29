# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import SUPERUSER_ID


def update_existing_attachment(cr, registry):
    obj_ir_attachment = registry["ir.attachment"]
    obj_ir_attachment_doc = registry["ir.attachment.document"]

    criteria = [
        ("res_id", "!=", False),
        ("res_model", "!=", False),
    ]
    attachment_ids = obj_ir_attachment.search(cr, SUPERUSER_ID, criteria, order="id")
    if attachment_ids:
        attachment = obj_ir_attachment.browse(cr, SUPERUSER_ID, attachment_ids)
        for data in attachment:
            value = {
                "res_id": data.res_id,
                "res_model": data.res_model,
                "res_name": data.res_name,
                "attachment_id": data.id,
            }
            obj_ir_attachment_doc.create(cr, SUPERUSER_ID, value)
