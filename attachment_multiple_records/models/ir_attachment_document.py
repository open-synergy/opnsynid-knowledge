# -*- coding: utf-8 -*-
# Copyright 2014 Savoir-faire Linux
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import fields, models


class IrAttachmentDocument(models.Model):
    _name = "ir.attachment.document"
    _description = "Attachment Documents"

    res_id = fields.Integer(
        string="Resource ID",
        readonly=True,
        help="The record id this is attached to.",
    )
    res_model = fields.Char(
        string="Resource Model",
        size=64,
        readonly=True,
        help="The database object this attachment will be attached to",
    )
    res_name = fields.Char(
        string="Resource Name",
        size=128,
        readonly=True,
    )
    attachment_id = fields.Many2one(
        string="Attachment",
        comodel_name="ir.attachment",
        ondelete="cascade",
    )
