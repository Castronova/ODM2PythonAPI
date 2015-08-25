__author__ = 'jmeline'

from .. import serviceBase
# from ...ODM2.models import *
from ODM2PythonAPI.src.api.ODM2 import models

# ################################################################################
# Annotations
# ################################################################################

def convertTupleToInt(tup):
    #  Gets the first integer inside tuple in a list
    return list(tup[0])[0]

class DeleteODM2(serviceBase):

    def test(self):
        return None

    '''Please keep these methods in alphabetical order'''

    def deleteActionBy_ByID(self, id):
        try:
            self._session.query(models.ActionBy).filter_by(ActionID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteActionByID(self, id):
        try:
            self._session.query(models.Actions).filter_by(ActionID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteAffiliationByID(self, id):
        try:
            self._session.query(models.Affiliations).filter_by(AffiliationID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteDatasetsByID(self, id):
        try:
            self._session.query(models.DataSets).filter_by(DatasetID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteFeatureActionByID(self, id):
        try:
            self._session.query(models.FeatureActions).filter_by(ActionID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteModelByID(self, id):
        try:
            self._session.query(models.Models).filter_by(ModelID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteModelByName(self, name):
        try:
            self._session.query(models.Models).filter_by(ModelName=name).delete()
            self._session.commit()
            pass
        except:
            return None

    def deleteOrganizationByID(self, id):
        try:
            self._session.query(models.Organizations).filter_by(OrganizationID=id).delete()
        except:
            return None

    def deletePeopleByID(self, id):
        try:
            self._session.query(models.People).filter_by(PersonID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteRecord(self, id):
        try:
            #  Simulation id an action id will not always be the same.
            #  So the action id id being used to delete the record
            id = self._session.query(models.Simulations.ActionID).filter_by(ActionID=id).all()
            id = convertTupleToInt(id)
            self.deleteSimulationByID(id)
            self.deleteActionByID(id)
            self.deleteActionBy_ByID(id)
            self.deleteResultByID(id)
            self.deleteFeatureActionByID(id)
            self.deleteTimeeSeriesResultByID(id)
            self.deleteDatasetsByID(id)
            pass
        except:
            return None

    def deleteResultByID(self, id):
        try:
            self._session.query(models.Results).filter_by(ResultID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteSimulationByID(self, id):
        try:
            self._session.query(models.Simulations).filter_by(SimulationID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteTimeeSeriesResultByID(self, id):
        try:
            self._session.query(models.TimeSeriesResults).filter_by(ResultID=id).delete()
            self._session.commit()
        except:
            return None

    def deleteUnitByID(self, id):
        try:
            self._session.query(models.Units).filter_by(UnitsID=id).delete()
            self._session.commit()
        except:
            return None

    def isModelConstraint(self, id):
        #  This methods returns True if a model is associated with a simulation.
        try:
            num = self._session.query(models.Simulations.SimulationName).filter(models.Simulations.ModelID == id).all()
            if len(num) < 1:
                return False
            else:
                return True
            pass
        except:
            return None




# ################################################################################
# CV
# ################################################################################





# ################################################################################
# Core
# ################################################################################




# ################################################################################
# Data Quality
# ################################################################################



# ################################################################################
# Equipment
# ################################################################################




# ################################################################################
# Extension Properties
# ################################################################################




# ################################################################################
# External Identifiers
# ################################################################################




# ################################################################################
# Lab Analyses
# ################################################################################




# ################################################################################
# Provenance
# ################################################################################




# ################################################################################
# Annotations
# ################################################################################




# ################################################################################
# Sampling Features
# ################################################################################




# ################################################################################
# Sensors
# ################################################################################




# ################################################################################
# ODM2
# ################################################################################

