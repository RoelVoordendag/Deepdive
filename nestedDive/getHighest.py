
def sum(orignalData, layers):
    print(orignalData)
    for x in range(layers):
        for name, data in orignalData.items():
            print(name)
            print(data)
        print(x)
    return "werkt de return zoals gemoeten"


testData = {
    "Charlois": {
            "Tarwewijk" : {
                "data": {
                    "Veiligheidsindex" : 73,
                    "Veiligheidsindex -subjectief" : 100
                }
            },
            "Carnisse" : {
                "data": {
                    "Veiligheidsindex" : 50,
                    "Veiligheidsindex -subjectief" : 102
                }
            },
            "ss" : {
                "data": {
                    "Veiligheidsindex" : 60,
                    "Veiligheidsindex -subjectief" : 60
                }
            }
    },
    "testing": {
            "wijk1" : {
                "data": {
                    "Veiligheidsindex" : 73,
                    "Veiligheidsindex -subjectief" : 50
                }
            },
            "wijk2" : {
                "id": 71,
                "data": {
                    "Veiligheidsindex" : 50,
                    "Veiligheidsindex -subjectief" : 100
                }
           },
    "ss" : {
                "data": {
                    "Veiligheidsindex" : 60,
                    "Veiligheidsindex -subjectief" : 100
                }
            }
    }
}


sum(testData,3)
