def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert list(dataset1.keys())==['archiveType', 'geo', 'data'], "Keys are incorrect"
    assert type(dataset1['geo']) == dict, 'geo should be a dictionary'
    assert list(dataset1['geo'].keys())==['lat', 'lon'], 'The keys of the "geo" dictionary are incorrect'
    assert type(dataset1['data']) == dict, 'data should be a dictionary'
    assert list(dataset1['data'].keys())==['values', 'units'], 'The keys of the "data" dictionary are incorrect'
    assert dataset1["archiveType"] == "marinesediment", "archiveType is incorrect"
    assert dataset1["geo"]['lat'] == -5, "lat is incorrect"
    assert dataset1["geo"]['lon'] == 140, "lon is incorrect"
    assert dataset1["data"]['units'] == 'N/A', "units is incorrect"
    assert type(dataset1["data"]['values']) == list, "The data values should be a list"
    assert dataset1["data"]['values'] == [1,2,3], "The data values are incorrect"
    assert latitude == -5, "latitude is incorrect"

    __msg__.good("Well done!")
