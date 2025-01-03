from odoo import models, api, fields

# Demo Task 02: In the order report template, 
# add new fields which must be visible in the pdf and add analytic distribution field.
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Creating a new field which will be calculated to get the analytic account name  
    analytic_account_name = fields.Char(string="Analytic", compute='_compute_analytic_account_name', store=False)

    #Creating a compute method to get the analytic account name from the analytic distribution record 
    def _compute_analytic_account_name(self):

        # Iterating loop over the records
        for line in self:
            
            # Checking if the record has value in analytic_distribution 
            if line.analytic_distribution:

                # Iterating in the record of analytic_distribution to get the ID
                for analytic_item in line.analytic_distribution.keys():
                    
                    if analytic_item: 

                        # Getting the analytic account name from the ID
                        analytic_account = self.env['account.analytic.account'].browse(int(analytic_item)).name
                        
                        if analytic_account:
                            
                            #Assiging value to the field and applying line which is a loop variable in the template                            
                            line.analytic_account_name = analytic_account
                            
                        else:
                            line.analytic_account_name = ''