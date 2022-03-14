# -*- coding: utf-8 -*-
# Copyright 2014 Savoir-faire Linux
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class IrAttachmentExistingDoc(models.TransientModel):
    _name = "ir.attachment.existing.doc"
    _description = "Add existing document/attachment wizard"

    attachment_ids = fields.Many2many(
        string="Attachments",
        comodel_name="ir.attachment",
        relation="rel_attachment_existing_wiz_2_attachment",
        column1="wizard_id",
        column2="attachment_id",
    )

    @api.multi
    def action_apply(self):
        obj_ir_attachment_document = self.env["ir.attachment.document"]
        active_model = self.env.context.get("model", False)
        active_ids = self.env.context.get("ids", False)
        obj_ir_model = self.env[active_model]

        name = obj_ir_model.browse(active_ids).name

        if not self.attachment_ids:
            raise UserError(
                _("Error"), _("You have to select at least 1 Document. And try again")
            )

        for attachment in self.attachment_ids:
            data = {
                "res_model": active_model,
                "res_id": active_ids[0],
                "res_name": name,
                "attachment_id": attachment.id,
            }
            # raise UserError(_("%s")%(data))
            obj_ir_attachment_document.create(data)
        return {"type": "ir.actions.act_window_close"}
