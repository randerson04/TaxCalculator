'''
textareademo.py
ry
ex from pg 276 -277 

gui based version of invesetment.py app from ch 3 
'''

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
	'''an inverstment calc that demos the use of a mulit line txt area'''
	def __init__(self):
		'''sets up window and widgets.'''
		EasyFrame.__init__(self, title = "Investment Calculator")
		#add label components
		self.addLabel(text = 'Inital amount', row = 0, column = 0)
		self.addLabel(text = 'Number of years', row =1 , column = 0)
		self.addLabel(text = 'Interest rate in %', row = 2, column = 0)
		#add entry field components 
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
		#add the text area comp
		self.outputArea = self.addTextArea(text = '', row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		#add btn component
		self.compute = self.addButton(text = "compute", row = 3, column = 0, columnspan = 2, command = self.compute) 
	def compute(self):
		'''computes the investment schedule based on the inputs and outputs the schedule'''
		#obtain and validate the inputs
		startBalance = self.amount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber() / 100

		#if any input is a zero, have the funct do nothing
		if startBalance == 0 or rate == 0 or years == 0:
			self.outputArea.setText("make sure none of the 3 fields have a value of zero!")
			return

		#initalize the accumulator for theinterest 
		totalIntrest = 0.0 

		#set the header for table
		result = '%4s%18s%10s%16s\n' % ('Year', 'Starting Balance', 'Interest', 
		'Ending Balance')
		#compute and append the results for each year
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += '%4d%18.2f%10.2f%16.2f\n' % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalIntrest += interest

		#append the totals for the entire investment period 
		result += 'Ending Balance: $%0.2f\n' % endBalance
		result += 'Total interest earned: $%0.2f\n' % totalIntrest

		#output the result var while preserving read-only status
		self.outputArea['state'] = 'normal'
		self.outputArea.setText(result)
		self.outputArea['state'] = 'disabled'

#def of the main() function
def main():
	TextAreaDemo().mainloop()

#global call to main() funct
main()
