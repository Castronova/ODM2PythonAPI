__author__ = 'tonycastronova'


import unittest
from ODM2PythonAPI.src.api.ODMconnection import dbconnection
from ODM2PythonAPI.src.api.ODM2.services.readService import ReadODM2
from ODM2PythonAPI.src.api.ODM2.services.createService import CreateODM2
from ODM2PythonAPI.src.api.ODM2.services.updateService import UpdateODM2
from ODM2PythonAPI.src.api.ODM2.services.deleteService import DeleteODM2



from sqlite3 import dbapi2 as sqlite

class test_sqlite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # build an empty database for testing
        conn = dbconnection.createConnection('sqlite', ':memory:')
        # dbconnection._setSchema(conn.engine)

        # build connectors for read, write, update, and delete operations
        cls.odmread = ReadODM2(conn)
        cls.odmcreate = CreateODM2(conn)
        cls.odmupdate = UpdateODM2(conn)
        cls.odmdelete = DeleteODM2(conn)

        # initialize the in-memory database, loop through each command (skip first and last lines)
        build = open('build_empty.sqlite').read()
        for line in build.split(';\n'):
            conn.getSession().execute(line)

        print 'database initialization completed successfully'

    @classmethod
    def tearDownClass(cls):
        del cls.odmread
        del cls.odmcreate
        del cls.odmupdate
        del cls.odmdelete

    def createPerson(self):

        # create some people
        self.odmcreate.createPerson(firstName="tony",
                                    lastName='castronova',
                                    middleName='michael')
        # this one should fail due to a not null constraint
        self.odmcreate.createPerson(firstName=None,
                                    lastName='castronova',
                                    middleName='michael')
        self.odmcreate.createPerson(firstName="tony",
                                    lastName='castronova',
                                    middleName=None)
        self.odmcreate.createPerson(firstName="john",
                                    lastName='doe')

        people = self.odmread.getPeople()
        self.assertTrue(len(people) == 3)


    def test_createVariable(self):

        # create some variables
        self.odmcreate.createVariable( code = 'Phos_TOT',
                                       name = 'Phosphorus, total dissolved',
                                       vType = 'Hydrology',
                                       nodv = -999,
                                       speciation =None ,
                                       definition =None )
        self.odmcreate.createVariable( code = 'Phos_TOT2',
                                       name = 'Phosphorus, total dissolved',
                                       vType = 'Hydrology',
                                       nodv = -999,
                                       speciation ='mg/L' ,
                                       definition =None )
        self.odmcreate.createVariable( code = 'Phos_TOT3',
                                       name = 'Phosphorus, total dissolved',
                                       vType = 'Hydrology',
                                       nodv = -999,
                                       speciation =None ,
                                       definition ='some definition' )
        # insert duplicate
        self.odmcreate.createVariable( code = 'Phos_TOT',
                                       name = 'Phosphorus, total dissolved',
                                       vType = 'Hydrology',
                                       nodv = -999,
                                       speciation =None ,
                                       definition =None )

        vars = self.odmread.getVariables()


        self.assertTrue(len(vars) == 3)


    def test_createMethod(self):
        self.odmcreate.createMethod(code ='mycode',
                                    name='my test method',
                                    vType='test method type',
                                    orgId=None,
                                    link=None,
                                    description='method description')
        self.odmcreate.createMethod(code ='mycode2',
                                    name='my test method',
                                    vType='test method type',
                                    orgId=1,
                                    link=None,
                                    description='method description')
        self.odmcreate.createMethod(code ='mycode3',
                                    name='my test method',
                                    vType='test method type',
                                    orgId=None,
                                    link=None,
                                    description=None)
        methods = self.odmread.getMethods()

        self.assertTrue(len(methods) == 3)


    def test_ProcessingLevel(self):

        self.odmcreate.createProcessingLevel(code="testlevel",
                                             definition="this is a test processing level",
                                             explanation=None)
        res = self.odmread.getProcessingLevels()

        self.assertTrue(len(res) == 1)


    def test_createSamplingFeature(self):


        res = self.odmread.getSamplingFeatures()

        self.assertTrue(len(res) == 1)

    def test_createUnit(self):

        res = self.odmread.getUnits()

        self.assertTrue(len(res) == 1)

    def test_createOrganization(self):
        res = self.odmread.getOrganizations()

        self.assertTrue(len(res) == 1)



    def test_createAffiliation(self):
        res = self.odmread.getAffiliationsByPerson()

        self.assertTrue(len(res) == 1)


    def test_createDataset(self):
        res = self.odmread.getDataSets()

        self.assertTrue(len(res) == 1)

    def test_createDatasetResults(self):
        res = self.odmread.getProcessingLevels()

        self.assertTrue(len(res) == 1)

    def test_createAction(self):
        # todo: this function is missing
        # res = self.odmread.getActions()

        self.assertTrue(0 == 1)

    def test_createActionBy(self):
        # todo; this function is missing
        # res = self.odmread.getActionsBy()

        self.assertTrue(0 == 1)

    def test_createFeatureAction(self):

        # todo: this function is missing
        # res = self.odmread.getFeatureActions()

        self.assertTrue(0 == 1)

    def test_createResult(self):
        res = self.odmread.getResults()

        self.assertTrue(len(res) == 1)

    def test_createTimeSeriesResult(self):
        res = self.odmread.getTimeSeriesResults()

        self.assertTrue(len(res) == 1)

    def test_createTimeSeriesResultValues(self):
        res = self.odmread.getTimeSeriesResultValues()

        self.assertTrue(len(res) == 1)

    def test_createSite(self):
        res = self.odmread.getAllSites()

        self.assertTrue(len(res) == 1)

    def test_createSpatialReference(self):
        res = self.odmread.getSpatialReferenceByCode()

        self.assertTrue(len(res) == 1)

    def test_createDeploymentAction(self):
        res = self.odmread.getAllDeploymentAction()

        self.assertTrue(len(res) == 1)

    def test_createModel(self):

        # create model  (expected: record inserted)
        self.odmcreate.createModel(code='model',
                                   name='mymodel',
                                   description='my test model')
        # create model with duplicate code (expected: fail to insert record)
        self.odmcreate.createModel(code='model',
                                   name='mymodel2',
                                   description='my test model2')
        # create with no description (expected: record inserted)
        self.odmcreate.createModel(code='model2',
                                   name='mymodel',
                                   description=None)

        res = self.odmread.getAllModels()

        self.assertTrue(len(res) == 2)

    def test_createRelatedModel(self):

        # create model  (expected: record inserted)
        m1 = self.odmcreate.createModel(code='model',
                                   name='mymodel',
                                   description='my test model')
        # create model  (expected: record inserted)
        m2 = self.odmcreate.createModel(code='model2',
                                   name='mymodel2',
                                   description='my test model2')
        # create a relationship type
        self.odmcreate.getSession().execute("insert into cv_relationshiptype values ('coupled', 'coupled model', 'models that have been coupled together', 'modeling', NULL)")

        # create related records
        self.odmcreate.createRelatedModel(modelid=m1.ModelID,
                                          relatedModelID=m2.ModelID,
                                          relationshipType='coupled')


        res = self.odmread.getRelatedModelsByCode('model')
        self.assertTrue(len(res) == 1)

        res = self.odmread.getRelatedModelsByCode('model2')
        self.assertTrue(len(res) == 0)


    def test_createSimulation(self):
        res = self.odmread.getAllSimulations()

        self.assertTrue(len(res) == 1)