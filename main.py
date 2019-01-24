from pandas_datareader import data
import matplotlib.pyplot as plt
import time

CURRENT_DATE = time.strftime('%Y-%m-%d')

def show_window(charts):
        #charts = list of charts you want to plot on screen (tickers, indicators, indices, etc)

        #note: maybe read these strings character by character and change settings (such as what plot to plot on, modify values, color, etc) end reading with a certain character
        start_date = '2010-01-01'
        nPlots = len(charts) #number of vertical plots total

        charts_data = [] #a list containing all of the close data for each ticker

        if (len(charts) != 1): #if you have multiple plots
                fig, charts_plots = plt.subplots(nPlots,1,sharex=True,sharey=False,figsize=(6,6)) #creates the subplots i need to understand tuple assignment
                plt.subplots_adjust(hspace=0.1) #horizontal space between plots
        
                for i in range(len(charts)): #loop through the multiple plots

                        #this appends the close price for each ticker, can be changed later.
                        charts_data.append(data.DataReader(charts[i], 'yahoo', start_date, CURRENT_DATE)['Adj Close']) #appends the 'adj close' of the data for the given ticker
                        charts_plots[i].set_ylabel(charts[i]) #set y labels for each plot

                        #formating stuff (not data specific)
                        charts_plots[i].plot(charts_data[i]) #plots the data for each corresponding plot (still need to understand)
                        charts_plots[i].tick_params(axis='x',which='both',bottom=False) #disable extra ticks on the top plots
                        charts_plots[i].grid(b=True,which='both',axis='both')
                        if (i == (len(charts)-1)):
                                charts_plots[i].tick_params(axis='x',which='both',bottom=True) #enable ticks for last plot

        else: #just 1 plot (therefore just the ticker, no anything else)
                charts_data.append(data.DataReader(charts[0], 'yahoo', start_date, CURRENT_DATE)['Adj Close'])
                plt.plot(charts_data[0])
                plt.grid(b=True,which='both',axis='both')
                plt.ylabel(charts[0])

        plt.show()

show_window(['AMD','SPY'])