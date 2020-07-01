# -*- coding: utf-8 -*-
# Copyright 2014 Savoir-faire Linux
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    @api.multi
    @api.depends(
        "res_model",
        "res_id",
    )
    def _name_get_resname(self):
        for attachment in self:
            attachment.res_name = False
            model_object = attachment.res_model
            res_id = attachment.res_id
            if model_object and res_id:
                model_pool = self.env[model_object]
                res = model_pool.browse(res_id).name_get()
                res_name = res and res[0][1] or False
                if res_name:
                    field = self._columns.get("res_name", False)
                    if field and len(res_name) > field.size:
                        res_name = res_name[:field.size - 3] + '...'
                attachment.res_name = res_name

    @api.model
    def _get_related_model_documents(self, operator, value):
        context = self.env.context
        res = [("id", "in", [])]
        obj_ir_attachment_document = \
            self.env["ir.attachment.document"]

        criteria = [
            ("res_model", "=", context.get("model")),
            ("res_id", "=", context.get("model_id"))]

        document_ids = \
            obj_ir_attachment_document.search(criteria)

        if document_ids:
            criteria_attachment = [
                ("attachment_document_ids.id", "in", document_ids.ids)
            ]
            attachment_ids = self.search(criteria_attachment)
            res = [("id", "in", attachment_ids.ids)]
        return res

    attachment_document_ids = fields.One2many(
        string="Records",
        comodel_name="ir.attachment.document",
        inverse_name="attachment_id"
    )
    res_name = fields.Char(
        string="Resource Name",
        size=128,
        compute="_name_get_resname",
        store=True,
    )
    related_document = fields.Boolean(
        string="Related Document",
        compute=lambda self: True,
        search="_get_related_model_documents",
    )

    @api.model
    def create(self, values):
        _super = super(IrAttachment, self)
        result = _super.create(values)

        obj_ir_attachment_document = \
            self.env["ir.attachment.document"]

        if "res_model" in values and "res_id" in values:
            res_name = result.res_name
            obj_ir_attachment_document.create({
                "attachment_id": result.id,
                "res_model": values["res_model"],
                "res_id": values["res_id"],
                "res_name": values.get("res_name", res_name),
            })
        return result

    @api.multi
    def unlink(self):
        _super = super(IrAttachment, self)
        result = _super.unlink()

        context = self._context

        obj_ir_attachment_document = \
            self.env["ir.attachment.document"]
        res_model = \
            context.get("multiple_records_res_model")
        res_id = \
            context.get("multiple_records_res_id")

        for document in self:
            if res_model and res_id:
                criteria = [
                    ("res_model", "=", res_model),
                    ("res_id", "=", res_id),
                    ("attachment_id", "=", document.id),
                ]
                ids_to_unlink = \
                    obj_ir_attachment_document.search(criteria)
                result = ids_to_unlink.unlink()
        return result
