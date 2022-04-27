#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('DSS for HELOC')
st.write('This is an application for a decision support system (DSS) that uses predictive modeling for evaluating the risk of Home Equity Line of Credit (HELOC). Please answer the following questions.')



# create a dataframe


df = pd.DataFrame(columns = ('ExternalRiskEstimate',
                             'NumSatisfactoryTrades',
                             'NumTrades60Ever2DerogPubRec',
                             'NumTrades90Ever2DerogPubRec',
                             'PercentTradesNeverDelq',
                             'MSinceMostRecentDelq',
                             'MaxDelq2PublicRecLast12M',
                             'MaxDelqEver',
                             'NumTotalTrades',
                             'NumTradesOpeninLast12M',
                             'PercentInstallTrades',
                             'MSinceMostRecentInqexcl7days',
                             'NumInqLast6M',
                             'NumInqLast6Mexcl7days',
                             'NetFractionRevolvingBurden',
                             'NetFractionInstallBurden',
                             'NumRevolvingTradesWBalance',
                             'NumInstallTradesWBalance',
                             'NumBank2NatlTradesWHighUtilization',
                             'MSinceMostRecentDelq=-7',
                             'MSinceMostRecentInqexcl7days=-7',
                             'MSinceMostRecentDelq=-8',
                             'MSinceMostRecentInqexcl7days=-8',
                             'NetFractionRevolvingBurden=-8',
                             'NetFractionInstallBurden=-8',
                             'NumRevolvingTradesWBalance=-8',
                             'NumInstallTradesWBalance=-8',
                             'NumBank2NatlTradesWHighUtilization=-8'
                            )
                 )


#ExternalRiskEstimate
ExternalRiskEstimate = st.number_input("Enter the level of external risk estimate",step=1)

#NumSatisfactoryTrades
NumSatisfactoryTrades = st.number_input("Enter the number of satisfactory trades",step=1)


#NumTrades60Ever2DerogPubRec
NumTrades60Ever2DerogPubRec = st.number_input("Enter the number of trades 60+ ever",step=1)


#NumTrades90Ever2DerogPubRec
NumTrades90Ever2DerogPubRec = st.number_input("Enter the number of trades 90+ ever",step=1)


#PercentTradesNeverDelq
PercentTradesNeverDelq = st.number_input("Enter the percent of trades never delinquent",step=1)


#MSinceMostRecentDelq
MSinceMostRecentDelq_option = st.selectbox(
    'Do you know the months since most recent delinquency?',
    ('Condition not Met (e.g. No Inquiries, No Delinquencies)', 'No Usable/Valid Trades or Inquiries', 'I have the data for the months since most recent delinquency.')
     )


if MSinceMostRecentDelq_option == 'I have the data for the months since most recent delinquency.':
    MSinceMostRecentDelq = st.number_input("Enter the months since most recent delinquency",step=1)
    MSinceMostRecentDelq_minus7 = 0
    MSinceMostRecentDelq_minus8 = 0
    
    st.write("The number of months since most recent delinquency is " + str(MSinceMostRecentDelq))

elif MSinceMostRecentDelq_option == 'Condition not Met (e.g. No Inquiries, No Delinquencies)':
    MSinceMostRecentDelq=21.86799007444169
    MSinceMostRecentDelq_minus7 = 1
    MSinceMostRecentDelq_minus8 = 0
    st.write("The number of months since most recent delinquency is replaced by the average number of months (21.87)")

else:
    MSinceMostRecentDelq=21.86799007444169
    MSinceMostRecentDelq_minus7 = 0
    MSinceMostRecentDelq_minus8 = 1
    st.write("The number of months since most recent delinquency is replaced by the average number of months (21.87)")



#MaxDelq2PublicRecLast12M
MaxDelq2PublicRecLast12M = st.number_input("Enter the max Delq/Public records last 12 months",min_value=0, max_value=9, step=1)


#MaxDelqEver
MaxDelqEver = st.number_input("Enter the max Delq/Public records ever",min_value=1, max_value=9, step=1)


#NumTotalTrades
NumTotalTrades = st.number_input("Enter the number of Total Trades (total number of credit accounts)", step=1)


#NumTradesOpeninLast12M
NumTradesOpeninLast12M = st.number_input("Enter the number of trades open in last 12 months", step=1)


#PercentInstallTrades
PercentInstallTrades = st.number_input("Enter the percent installment trades", step=1)


#MSinceMostRecentInqexcl7days


MSinceMostRecentInqexcl7days_option = st.selectbox(
    'Do you know the months since most recent delinquency?',
    ('Condition not Met (e.g. No Inquiries, No Delinquencies)', 'No Usable/Valid Trades or Inquiries', 'I have the data for the months since most recent inquries excluding 7days.')
     )

if MSinceMostRecentInqexcl7days_option == 'I have the data for the months since most recent inquries excluding 7days.':
    MSinceMostRecentInqexcl7days = st.number_input("Enter the months since most recent inquries excluding 7days", step=1)
    MSinceMostRecentInqexcl7days_minus7 = 0
    MSinceMostRecentInqexcl7days_minus8 = 0
    st.write("The number of months since most recent inquries excluding 7days is " + str(MSinceMostRecentInqexcl7days))

elif MSinceMostRecentInqexcl7days_option == 'Condition not Met (e.g. No Inquiries, No Delinquencies)':
    MSinceMostRecentInqexcl7days=2.4893158853735295
    MSinceMostRecentInqexcl7days_minus7 = 1
    MSinceMostRecentInqexcl7days_minus8 = 0
    st.write("The number months since most recent inquries excluding 7days is replaced by the average number of months (2.49)")

else:
    MSinceMostRecentInqexcl7days=2.4893158853735295
    MSinceMostRecentInqexcl7days_minus7 = 0
    MSinceMostRecentInqexcl7days_minus8 = 1
    st.write("The number of months since most recent inquries excluding 7days is replaced by the average number of months (2.49)")


#NumInqLast6M
NumInqLast6M = st.number_input("Enter the number of inquries in last 6 months", step=1)


#NumInqLast6Mexcl7days
NumInqLast6Mexcl7days = st.number_input("Enter the number of inquries in last 6 months excluding 7 days.", step=1)


#NetFractionRevolvingBurden


NetFractionRevolvingBurden_option = st.selectbox(
    'Do you know the net fraction revolving burden?',
    ('No Usable/Valid Trades or Inquiries', 'I have the data for the net fraction revolving burden.')
     )

if NetFractionRevolvingBurden_option == 'I have the data for the net fraction revolving burden.':
    NetFractionRevolvingBurden = st.number_input("Enter the net fraction revolving burden. This is revolving balance divided by credit limit.", step=1)
    NetFractionRevolvingBurden_minus8 = 0
    st.write("The net fraction revolving burden is " + str(NetFractionRevolvingBurden))

else:
    NetFractionRevolvingBurden=34.903010033444815
    NetFractionRevolvingBurden_minus8 = 1
    st.write("The the net fraction revolving burden is replaced by the average number (34.90)")


#NetFractionInstallBurden

NetFractionInstallBurden_option = st.selectbox(
    'Do you know the net fraction installment burden.?',
    ('No Usable/Valid Trades or Inquiries', 'I have the data for the net fraction installment burden.')
     )

if NetFractionInstallBurden_option == 'I have the data for the net fraction installment burden.':
    NetFractionInstallBurden = st.number_input("Enter the net fraction installment burden. This is installment balance divided by original loan amount.", step=1)
    NetFractionInstallBurden_minus8 = 0
    st.write("The net fraction installment burden " + str(NetFractionInstallBurden))

else:
    NetFractionInstallBurden=68.52943447210963
    NetFractionInstallBurden_minus8 = 1
    st.write("The the net fraction installment burden is replaced by the average number (68.53)")

#NumRevolvingTradesWBalance

NumRevolvingTradesWBalance_option = st.selectbox(
    'Do you know the number of revolving trades with balance?',
    ('No Usable/Valid Trades or Inquiries', 'I have the data for the number of revolving trades with balance.')
     )

if NumRevolvingTradesWBalance_option == 'I have the data for the number of revolving trades with balance.':
    NumRevolvingTradesWBalance = st.number_input("Enter the number of revolving trades with balance.", step=1)
    NumRevolvingTradesWBalance_minus8 = 0
    st.write("The number of revolving trades with balance is " + str(NumRevolvingTradesWBalance))

else:
    NumRevolvingTradesWBalance=34.903010033444815
    NumRevolvingTradesWBalance_minus8 = 1
    st.write("The the net fraction revolving burden is replaced by the average number (34.90)")

#NumInstallTradesWBalance

NumInstallTradesWBalance_option = st.selectbox(
    'Do you know the number of installment trades with balance?',
    ('No Usable/Valid Trades or Inquiries', 'I have the data for the number of installment trades with balance.')
     )

if NumInstallTradesWBalance_option == 'I have the data for the number of installment trades with balance.':
    NumInstallTradesWBalance = st.number_input("Enter the number of installment trades with balance", step=1)
    NumInstallTradesWBalance_minus8 = 0
    st.write("The number of installment trades with balance " + str(NumInstallTradesWBalance))

else:
    NumInstallTradesWBalance=2.49
    NumInstallTradesWBalance_minus8 = 1
    st.write("The number of installment trades with balance is replaced by the average number (2.49)")

#NumBank2NatlTradesWHighUtilization

NumBank2NatlTradesWHighUtilization_option = st.selectbox(
    'Do you know the number of bank/natl trades with high utilization ratio?',
    ('No Usable/Valid Trades or Inquiries', 'I have the data for the number of bank/natl trades with high utilization ratio.')
     )

if NumBank2NatlTradesWHighUtilization_option == 'I have the data for the number of bank/natl trades with high utilization ratio.':
    NumBank2NatlTradesWHighUtilization = st.number_input("Enter the number of bank/natl trades with high utilization ratio", step=1)
    NumBank2NatlTradesWHighUtilization_minus8 = 0
    st.write("The number of bank/natl trades with high utilization ratio is " + str(NumBank2NatlTradesWHighUtilization))

else:
    NumBank2NatlTradesWHighUtilization=1.0896800963726407
    NumBank2NatlTradesWHighUtilization_minus8 = 1
    st.write("The number of bank/natl trades with high utilization ratio is replaced by the average number (1.09)")


df.loc[0]=[ExternalRiskEstimate,
           NumSatisfactoryTrades,
           NumTrades60Ever2DerogPubRec,
           NumTrades90Ever2DerogPubRec,
           PercentTradesNeverDelq,
           MSinceMostRecentDelq,
           MaxDelq2PublicRecLast12M,
           MaxDelqEver,
           NumTotalTrades,
           NumTradesOpeninLast12M,
           PercentInstallTrades,
           MSinceMostRecentInqexcl7days,
           NumInqLast6M,
           NumInqLast6Mexcl7days,
           NetFractionRevolvingBurden,
           NetFractionInstallBurden,
           NumRevolvingTradesWBalance,
           NumInstallTradesWBalance,
           NumBank2NatlTradesWHighUtilization,
           MSinceMostRecentDelq_minus7,
           MSinceMostRecentInqexcl7days_minus7,
           MSinceMostRecentDelq_minus8,
           MSinceMostRecentInqexcl7days_minus8,
           NetFractionRevolvingBurden_minus8,
           NetFractionInstallBurden_minus8,
           NumRevolvingTradesWBalance_minus8, 
           NumInstallTradesWBalance_minus8,
           NumBank2NatlTradesWHighUtilization_minus8
           ]

st.header('Estimated Outcome')
#st.dataframe(df)

import pickle



# Model

# open model

with open("Boosting_model.p","rb") as f2 : 
    loaded_model = pickle.load(f2)

prediction = loaded_model.predict(df)

st.write('These is the prediction using the model that was loaded from the input values:')



if prediction  == 1 :
    st.markdown("You should **_reject_** the application! Estimated outcome indicates that the applicant was 90 days past due or worse at least once over a period of 24 months from when the credit account was opened. ")
else:
    st.markdown("You should **_accept_** the application! Estimated outcome indicates that the applicant made their payments without ever being more than 90 days overdue. ")







