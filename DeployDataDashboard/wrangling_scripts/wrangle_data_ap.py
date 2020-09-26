import pandas as pd
import plotly.graph_objs as go


def cleandata(dataset, keepcolumns = ['Reference Area', 'Time Period', 'Observation Value']):
    """Clean UN data for a visualizaiton dashboard

    Keeps data in keep_columns variable and data for the SAARC countries    
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        df

    """    
    df = pd.read_csv(dataset)

    # Keep only the columns of interest (Reference Ares, Time Period and Observation Value)
    df = df[keepcolumns]
    # Country list of interest
    country_saarc = ['Afghanistan', 'Bangladesh', 'Bhutan','India','Nepal', 'Pakistan']
    df = df[df['Reference Area'].isin(country_saarc)]
    # output clean csv file
    return df

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  # first chart plots 
    
    graph_one = []
    df = cleandata('data/UNdata_Export_20200922_021257174.csv')
    df.columns = ['country','year','percentage']
    countrylist = df.country.unique().tolist() 
    
    list_years=[]    
    for country in countrylist:
        yrs= df[df['country'] == country].year.tolist()
        list_years.append(yrs)
    #Finding common year
    """[1984, 1977, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]"""
    common_years=set(list_years[0]).intersection(*list_years)
    common_years=list(common_years)
    common_years.sort() 
    '''Data frame with only common Years'''
    df=df.loc[df['year'].isin(common_years)]

    for country in countrylist:
      x_val = df[df['country'] == country].year.tolist()
      y_val =  df[df['country'] == country].percentage.tolist()
      graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
      )

    layout_one = dict(title = 'Percentage of girls in secondary level <br> 1977 to 2013',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Percentage'),
                )

# second chart plots percentage for a Year as a bar chart    
    graph_two = []
    df = cleandata('data/UNdata_Export_20200922_021257174.csv')
    df.columns = ['country','year','percentage']
    #df.sort_values('percentage', ascending=False, inplace=True)
    '''Taking just first value from 1977'''
    df = df[df['year'] == common_years[0]] 

    graph_two.append(
      go.Bar(
      x = df.country.tolist(),
      y = df.percentage.tolist(),
      )
    )

    layout_two = dict(title = 'Percentage of girls in secondary level in 1977',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Percentage'),
                )

# third chart plots percentage for the highest Year as a bar chart    
    graph_three = []
    df = cleandata('data/UNdata_Export_20200922_021257174.csv')
    df.columns = ['country','year','percentage']
    #df.sort_values('percentage', ascending=False, inplace=True)
    '''Taking just first value from 2013'''
    df = df[df['year'] == common_years[-1]]

    graph_three.append(
      go.Bar(
      x = df.country.tolist(),
      y = df.percentage.tolist(),
      )
    )

    layout_three = dict(title = 'Percentage of girls in secondary level in 2013',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Percentage'),
                )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))

    return figures
