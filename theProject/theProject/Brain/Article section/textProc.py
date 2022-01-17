import pandas as pd 
import resources
import tckrDict from resources
import impWordDictGood from resources
import impWordDictBad from resources
import impWordDictAll from resources
import currencyDict from resources
import cammodityDict from resources
import countryDict from resources



def textProc(text):
    tckrCountList = []
    impWordTckrDistListAll = []
    impWordTckrDistListGood = []
    impWordTckrDistListBad = []

    impWordCountListGood = []
    impWordCountListBad = []
    impWordCountListAll = []
    iWouldBuyCount = 0

    currencyCountList = []
    impWordCurrencyDistListAll = []
    impWordCurrencyDistListGood = []
    impWordCurrencyDistListBad = []

    cammodityCountList = []
    impWordCammodityDistListAll = []
    impWordCammodityDistListGood = []
    impWordCammodityDistListBad = []

    countryCountList = []
    impWordCountryDistListAll = []
    impWordCountryDistListGood = []
    impWordCountryDistListBad = []
    t=0
    text.lower(all)
    for i in text:
        
        if i in tckrDict:
            # ticker text counter
            tckrCountList.append(i)
            for z in range(-10, 10):
                if text[t+(z)] in impWordDictAll:
                    impWordTckrDistListAll.append(f"{text[i+(z)]} is {z} from {i}")
                elif text[t+(z)] in impWordDictGood:
                    impWordTckrDistListGood.append(f"{text[t+(z)]} is {z} from {i}")
                elif text[t+(z)] in impWordDictBad:
                    impWordTckrDistListBad.append(f"{text[t+(z)]} is {z} from {i}")
                else:
                    pass
        if i in currencyDict:
            # currency text counter
            currencyCountList.append(i)
            for z in range(-10, 10):
                if text[t+(z)] in impWordDictAll:
                    impWordCurrencyDistListAll.append(f"{text[t+(z)]} is {i} from {i}")
                elif text[t+(z)] in impWordDictGood:
                    impWordCurrencyDistListGood.append(f"{text[t+(z)]} is {z} from {i}")
                elif text[t+(z)] in impWordDictBad:
                    impWordCurrencyDistListBad.append(f"{text[t+(z)]} is {z} from {i}")
                else:
                    pass

        if i in cammodityDict:
            # cammodity text counter
            cammodityCountList.append(i)
            for z in range(-10, 10):
                if text[t+(z)] in impWordDictAll:
                    impWordCammodityDistListAll.append(f"{text[t+(z)]} is {z} from {i}")
                elif text[t+(z)] in impWordDictGood:
                    impWordCammodityDistListGood.append(f"{text[t+(z)]} is {z} from {i}")
                elif text[t+(z)] in impWordDictBad:
                    impWordCammodityDistListBad.append(f"{text[t+(z)]} is {z} from {i}")
                else:
                    pass
        if i in countryDict:
            # Country text counter
            countryCountList.append(i)
            for z in range(-10, 10):
                if text[t+(z)] in impWordDictAll:
                    impWordCountryDistListAll.append(f"{text[t+(z)]} is {z} from {i}")
                elif text[t+(z)] in impWordDictGood:
                    impWordCountryDistListGood.append(f"{text[t+(z)]} is {z} from {i}")
                elif text[t+(z)] in impWordDictBad:
                    impWordCountryDistListBad.append(f"{text[t+(z)]} is {z} from {i}")
                else:
                    pass
        # imp word list appenders
        elif i in impWordDictGood:
            impWordCountListGood.append(i)

        elif i in impWordList:
            impWordCountListBad.append(i)

        elif i in impWordDictAll:
            impWordCountListAll.append(i)

#       try to count if someone states they would buy the stock
        elif i == "buy" & text[i-1]== "would" & text[i-2]== "i":
            iWouldBuyCount+=1
        t+=1

            


# which ticker is talked about the most
    maneTckr = tckrCountList.mode()

# taking in info from the distance  from loops with tickers
    tdf = pd.DataFrame('tckrCount': tckrCountList)
    tckrCounts = tdf.groupby(tckrCount).count()

    ddf = pd.DataFrame('impWordTckrDistListAll': impWordTckrDistListAll)
    impWordTckrDistCountAll = ddf.groupby(impWordTckrDistListAll).count()

    ddf = pd.DataFrame('impWordTckrDistListGood': impWordTckrDistListGood)
    impWordTckrDistCountGood = ddf.groupby(impWordTckrDistListGood).count()

    ddf = pd.DataFrame('impWordTckrDistListBad': impWordTckrDistListBad)
    impWordTckrDistCountBad = ddf.groupby(impWordTckrDistListBad).count()

# taking in info from the distance from loops with currencies
    df = pd.DataFrame('currencyCount': currencyCountList)
    currencyCounts = df.groupby(currencyCount).count()

    df = pd.DataFrame('impWordCurrencyDistListAll': impWordCurrencyDistListAll)
    impWordCurrencyDistCountAll = df.groupby(impWordCurrencyDistListAll).count()

    df = pd.DataFrame('impWordCurrencyDistListGood': impWordCurrencyDistListGood)
    impWordCurrencyDistCountGood = df.groupby(impWordCurrrencyDistListGood).count()

    df = pd.DataFrame('impWordCurrencyDistListBad': impWordCurrencyDistListBad)
    impWordCurrencyDistCountBad = df.groupby(impWordCurrencyDistListBad).count()

# taking in info from the distance from loops with cammodities
    tdf = pd.DataFrame('cammodityCount': cammodityCountList)
    cammodityCounts = tdf.groupby(cammodityCount).count()

    ddf = pd.DataFrame('impWordCammodityDistListAll': impWordCammodityDistListAll)
    impWordCammodityDistCountAll = ddf.groupby(impWordCammodityDistListAll).count()

    ddf = pd.DataFrame('impWordCammodityDistListGood': impWordCammodityDistListGood)
    impWordCammodityDistCountGood = ddf.groupby(impWordCammodityDistListGood).count()

    ddf = pd.DataFrame('impWordCammodityDistListBad': impWordCammodityDistListBad)
    impWordCammodityDistCountBad = ddf.groupby(impWordCammodityDistListBad).count()

# taking in info from the distance from loops with country
    tdf = pd.DataFrame('countryCount': countryCountList)
    countryCounts = tdf.groupby(countryCount).count()

    ddf = pd.DataFrame('impWordCountryDistListAll': impWordCountryDistListAll)
    impWordCammodityDistCountAll = ddf.groupby(impWordCammodityDistListAll).count()

    ddf = pd.DataFrame('impWordCountryDistListGood': impWordCountryDistListGood)
    impWordCountryDistCountGood = ddf.groupby(impWordCountryDistListGood).count()

    ddf = pd.DataFrame('impWordCammodityDistListBad': impWordCammodityDistListBad)
    impWordCountryDistCountBad = ddf.groupby(impWordCountryDistListBad).count()
    
# counting all good, bad and total important words 
    gdf = pd.DataFrame('impWordCountListGood': impWordCountListGood)
    impWordCountGood = gdf.groupby(impWordCountListGood).count()

    bdf = pd.DataFrame('impWordCountListBad': impWordCountListBad)
    impWordCountBad = bdf.groupby(impWordCountListBad.count()

    adf = pd.DataFrame('impWordCountListAll': impWordCountListAll)
    
# finding concentrations of good, bad and all important words
    impWordCountAll = adf.groupby(impWordCountListAll).count()
    empWordConcentration = len(text)/len(impWordCountListAll)
    empWordConcentrationGood = len(text)/len(impWordCountListGood)
    empWordConcentrationBad = len(text)/len(impWordCountListBad)


    dict = {
        "maneTckr": maneTckr,
        "tckrCounts" : tckrCounts,
        "impWordTckrDistCountAll": impWordTckrDistCountAll,
        "impWordTckrDistCountGood": impWordTckrDistCountGood,
        "impWordTckrDistCountBad": impWordTckrDistCountBad,
        "impWordTckrDistList": impWordTckrDistListAll,
        "currencyCounts": currencyCounts,
        "impWordCurrencyDistList": impWordCurrencyDistListAll,
        "impWordCurrencyDistCountAll": impWordCurrencyDistCountAll,
        "impWordCurrencyDistCountGood": impWordCurrencyDistCountGood,
        "impWordCurrencyDistCountBad": impWordCurrencyDistCountBad,
        "cammodityCounts": cammodityCounts,
        "impWordCammodityDistList": impWordCammodityDistListAll,
        "impWordCammodityDistCountAll": impWordCammodityDistCountAll,
        "impWordCammodityDistCountGood": impWordCammodityDistCountGood,
        "impWordCammodityDistCountBad": impWordCammodityDistCountBad,
        "countryCounts": countryCounts,
        "impWordCountryDistList": impWordCountryDistListAll,
        "impWordCountryDistCountAll": impWordCountryDistCountAll,
        "impWordCountryDistCountGood": impWordCountryDistCountGood,
        "impWordCountryDistCountBad": impWordCountryDistCountBad,       
        "impWordCountGood": impWordCountGood,
        "impWordCountBad": impWordCountBad,
        "impWordCountAll": impWordCountAll,
        "empWordConcentration": empWordConcentration,
        "empWordConcentrationGood": empWordConcentrationGood,
        "empWordConcentrationBad": empWordConcentrationBad,
        "iWouldBuyCount": iWouldBuyCount
    }