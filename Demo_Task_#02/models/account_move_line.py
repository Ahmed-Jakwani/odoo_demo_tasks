from odoo import api, fields, models

# Demo Task 02: In the report template of account.move,  
# add new fields which must be visible in the pdf and add analytic distribution field.
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # Creating a new field which will be calculated to get the analytic account name  
    analytic_account_name = fields.Char(string="Analytic", compute='_compute_analytic_account_name')

    def _compute_analytic_account_name(self):

        for line in self:
            
            line.analytic_account_name = ''
            
            # Checking if the record has value in analytic_distribution 
            if line.analytic_distribution:

                # Iterating in the record of analytic_distribution to get the ID
                for analytic_item in line.analytic_distribution.keys():
                    
                    if analytic_item: 

                        # Getting the analytic account name from the ID
                        analytic_account = self.env['account.analytic.account'].browse(int(analytic_item)).name
                        
                        if analytic_account:
                            
                            # Assiging value to the field                         
                            line.analytic_account_name = analytic_account
                        
                            
                    