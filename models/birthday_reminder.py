from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(string="Birthday")

    @api.model
    def check_birthday_reminders(self):
        today = fields.Date.today()
        upcoming_birthdays = self.search([('birthday', '=', today)])
        for partner in upcoming_birthdays:
            if partner.email:
                template = self.env.ref('birthday_reminder.birthday_email_template')
                if template:
                    template.send_mail(partner.id, force_send=True)