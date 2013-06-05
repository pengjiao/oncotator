"""
# By downloading the PROGRAM you agree to the following terms of use:
#
# BROAD INSTITUTE SOFTWARE LICENSE AGREEMENT
# FOR ACADEMIC NON-COMMERCIAL RESEARCH PURPOSES ONLY
#
# This Agreement is made between the Broad Institute, Inc. with a principal address at 7 Cambridge Center, Cambridge, MA 02142 ("BROAD") and the LICENSEE and is effective at the date the downloading is completed ("EFFECTIVE DATE").
# WHEREAS, LICENSEE desires to license the PROGRAM, as defined hereinafter, and BROAD wishes to have this PROGRAM utilized in the public interest, subject only to the royalty-free, nonexclusive, nontransferable license rights of the United States Government pursuant to 48 CFR 52.227-14; and
# WHEREAS, LICENSEE desires to license the PROGRAM and BROAD desires to grant a license on the following terms and conditions.
# NOW, THEREFORE, in consideration of the promises and covenants made herein, the parties hereto agree as follows:
#
# 1. DEFINITIONS
# 1.1	"PROGRAM" shall mean copyright in the object code and source code known as Oncotator and related documentation, if any, as they exist on the EFFECTIVE DATE and can be downloaded from http://www.broadinstitute.org/cancer/cga/oncotator on the EFFECTIVE DATE.
#
# 2. LICENSE
# 2.1   Grant. Subject to the terms of this Agreement, BROAD hereby grants to LICENSEE, solely for academic non-commercial research purposes, a non-exclusive, non-transferable license to: (a) download, execute and display the PROGRAM and (b) create bug fixes and modify the PROGRAM.
# LICENSEE hereby automatically grants to BROAD a non-exclusive, royalty-free, irrevocable license to any LICENSEE bug fixes or modifications to the PROGRAM with unlimited rights to sublicense and/or distribute.  LICENSEE agrees to provide any such modifications and bug fixes to BROAD promptly upon their creation.
# The LICENSEE may apply the PROGRAM in a pipeline to data owned by users other than the LICENSEE and provide these users the results of the PROGRAM provided LICENSEE does so for academic non-commercial purposes only.  For clarification purposes, academic sponsored research is not a commercial use under the terms of this Agreement.
# 2.2  No Sublicensing or Additional Rights. LICENSEE shall not sublicense or distribute the PROGRAM, in whole or in part, without prior written permission from BROAD.  LICENSEE shall ensure that all of its users agree to the terms of this Agreement.  LICENSEE further agrees that it shall not put the PROGRAM on a network, server, or other similar technology that may be accessed by anyone other than the LICENSEE and its employees and users who have agreed to the terms of this agreement.
# 2.3  License Limitations. Nothing in this Agreement shall be construed to confer any rights upon LICENSEE by implication, estoppel, or otherwise to any computer software, trademark, intellectual property, or patent rights of BROAD, or of any other entity, except as expressly granted herein. LICENSEE agrees that the PROGRAM, in whole or part, shall not be used for any commercial purpose, including without limitation, as the basis of a commercial software or hardware product or to provide services. LICENSEE further agrees that the PROGRAM shall not be copied or otherwise adapted in order to circumvent the need for obtaining a license for use of the PROGRAM.
#
# 3. OWNERSHIP OF INTELLECTUAL PROPERTY
# LICENSEE acknowledges that title to the PROGRAM shall remain with BROAD. The PROGRAM is marked with the following BROAD copyright notice and notice of attribution to contributors. LICENSEE shall retain such notice on all copies.  LICENSEE agrees to include appropriate attribution if any results obtained from use of the PROGRAM are included in any publication.
#
# Copyright 2012 Broad Institute, Inc.
# Notice of attribution:  The Oncotator program was made available through the generosity of the Cancer Genome Analysis group at the Broad Institute, Inc.
#
# LICENSEE shall not use any trademark or trade name of BROAD, or any variation, adaptation, or abbreviation, of such marks or trade names, or any names of officers, faculty, students, employees, or agents of BROAD except as states above for attribution purposes.
#
# 4. INDEMNIFICATION
# LICENSEE shall indemnify, defend, and hold harmless BROAD, and their respective officers, faculty, students, employees, associated investigators and agents, and their respective successors, heirs and assigns, ("Indemnitees"), against any liability, damage, loss, or expense (including reasonable attorneys fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, actions, demands or judgments arising out of any theory of liability (including, without limitation, actions in the form of tort, warranty, or strict liability and regardless of whether such action has any factual basis) pursuant to any right or license granted under this Agreement.
#
# 5. NO REPRESENTATIONS OR WARRANTIES
# THE PROGRAM IS DELIVERED "AS IS."  BROAD MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE PROGRAM OR THE COPYRIGHT, EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, WHETHER OR NOT DISCOVERABLE. BROAD EXTENDS NO WARRANTIES OF ANY KIND AS TO PROGRAM CONFORMITY WITH WHATEVER USER MANUALS OR OTHER LITERATURE MAY BE ISSUED FROM TIME TO TIME.
# IN NO EVENT SHALL BROAD OR ITS RESPECTIVE DIRECTORS, OFFICERS, EMPLOYEES, AFFILIATED INVESTIGATORS AND AFFILIATES BE LIABLE FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES OF ANY KIND, INCLUDING, WITHOUT LIMITATION, ECONOMIC DAMAGES OR INJURY TO PROPERTY AND LOST PROFITS, REGARDLESS OF WHETHER BROAD SHALL BE ADVISED, SHALL HAVE OTHER REASON TO KNOW, OR IN FACT SHALL KNOW OF THE POSSIBILITY OF THE FOREGOING.
#
# 6. ASSIGNMENT
# This Agreement is personal to LICENSEE and any rights or obligations assigned by LICENSEE without the prior written consent of BROAD shall be null and void.
#
# 7. MISCELLANEOUS
# 7.1 Export Control. LICENSEE gives assurance that it will comply with all United States export control laws and regulations controlling the export of the PROGRAM, including, without limitation, all Export Administration Regulations of the United States Department of Commerce. Among other things, these laws and regulations prohibit, or require a license for, the export of certain types of software to specified countries.
# 7.2 Termination. LICENSEE shall have the right to terminate this Agreement for any reason upon prior written notice to BROAD. If LICENSEE breaches any provision hereunder, and fails to cure such breach within thirty (30) days, BROAD may terminate this Agreement immediately. Upon termination, LICENSEE shall provide BROAD with written assurance that the original and all copies of the PROGRAM have been destroyed, except that, upon prior written authorization from BROAD, LICENSEE may retain a copy for archive purposes.
# 7.3 Survival. The following provisions shall survive the expiration or termination of this Agreement: Articles 1, 3, 4, 5 and Sections 2.2, 2.3, 7.3, and 7.4.
# 7.4 Notice. Any notices under this Agreement shall be in writing, shall specifically refer to this Agreement, and shall be sent by hand, recognized national overnight courier, confirmed facsimile transmission, confirmed electronic mail, or registered or certified mail, postage prepaid, return receipt requested.  All notices under this Agreement shall be deemed effective upon receipt.
# 7.5 Amendment and Waiver; Entire Agreement. This Agreement may be amended, supplemented, or otherwise modified only by means of a written instrument signed by all parties. Any waiver of any rights or failure to act in a specific instance shall relate only to such instance and shall not be construed as an agreement to waive any rights or fail to act in any other instance, whether or not similar. This Agreement constitutes the entire agreement among the parties with respect to its subject matter and supersedes prior agreements or understandings between the parties relating to its subject matter.
# 7.6 Binding Effect; Headings. This Agreement shall be binding upon and inure to the benefit of the parties and their respective permitted successors and assigns. All headings are for convenience only and shall not affect the meaning of any provision of this Agreement.
# 7.7 Governing Law. This Agreement shall be construed, governed, interpreted and applied in accordance with the internal laws of the Commonwealth of Massachusetts, U.S.A., without regard to conflict of laws principles.
#"""
from oncotator.Annotation import Annotation


"""
Created on Nov 2, 2012

@author: lichtens
"""
from input.InputMutationCreator import InputMutationCreator
from oncotator.utils.MutUtils import MutUtils
from output.OutputRenderer import OutputRenderer
import logging
from utils.version import VERSION
    
class Annotator(object):
    """
    The Annotator is the entry point to actually perform the annotating of mutations.  The Annotator contains one input creator (IC), one output creator (OC), and a list of datasources.   
    
    This class is responsible for the coordination of the annotating process, not the annotations themselves (this is handled by the datasources).
    
    For information on how to initialize the input and output creator, please see the documentation of those classes.

    See the RunSpecification class, which allows for more control
        of an annotator.

    Example usage (with RunSpec and no multicore usage):
    # Create a run configuration to pass to the Annotator class.  See OncotatorCLIUtils.getSupportedOutputFormats()
    #   and OncotatorCLIUtils.getSupportedInputFormats() for allowed inputFormat and outputFormat strings.
    manualOverrides = {'fake_annotation':'picard', 'fake_annotation2':'worf'}
    runConfig = OncotatorCLIUtils.createRunConfig(inputFormat, outputFormat, inputFilename, outputFilename, globalAnnotations=manualOverrides, datasourceDir="/home/onco/dbs", isMulticore=False)

    annotator = Annotator()
    annotator.initialize(runConfig)
    annotator.annotate()

    Example usage (used in testing, without RunSpec):
        # Assumed myIC and myOC have been initialized as the proper Input and Output Creators, respectively.
        # 1) Initialize the Annotator
        annotator = Annotator()
        annotator.setInputCreator(myIC)
        annotator.setOutputCreator(myOC)
        # 1a) For each datasource (instance of a datasource class), add it to the annotator.
        for datasource in myDataSources:
            annotator.addDatasource(datasource)
        # 2)  Produce the output
        filePointer = annotator.annotate()
    
    NOTE:  While multicore information is passed into the Annotator, currently, nothing is implemented that uses multicore.    
    """

    def __init__(self):
        """
        options should contain the following name-value pairs as a dict: 
        
        Create a new instance of Annotator.
        
        In order to specify the input and output creators and datasources, use the set and addDatasource methods.
        
        """
        self._inputCreator = None
        self._outputRenderer = None
        self._datasources = []
        self.logger = logging.getLogger(__name__)
        self._manualAnnotations = dict()
        self._isMulticore = None
        self._numCores = None
        pass

    def getIsMulticore(self):
        return self.__isMulticore


    def getNumCores(self):
        return self.__numCores


    def setIsMulticore(self, value):
        self.__isMulticore = value


    def setNumCores(self, value):
        self.__numCores = value

    
    def setInputCreator(self, inputCreator):
        self._inputCreator = inputCreator
        
    def setOutputRenderer(self, outputCreator):
        self._outputRenderer = outputCreator
    
    def setManualAnnotations(self, value):
        self._manualAnnotations = value
           
               
    def initialize(self,runSpec):
        """ Given a RunSpecification instance, initialize self properly.  Do not start annotation.
        """
        self.setInputCreator(runSpec.inputCreator)
        self.setOutputRenderer(runSpec.outputRenderer)
        self.setManualAnnotations(runSpec.manualAnnotations)
        self._datasources = runSpec.datasources
        self.setIsMulticore(runSpec.get_is_multicore())
        self.setNumCores(runSpec.get_num_cores())

    def addDatasource(self, datasource):
        self._datasources.append(datasource)

    def _createMetadata(self):
        metadata = self._inputCreator.getMetadata()
        metadata.update(self._createManualAnnotationsForMetadata(self._manualAnnotations))
        return metadata

    def _createComments(self):
        comments = self._inputCreator.getComments()
        comments.append(self.createHeaderString())
        return comments

    def annotate(self):
        """
        Annotate the given mutations specified in the input.

        Call this after the input, output, and datasources have been set.

        :return: outputFilename
        """
        self.logger.info("Annotating with " + str(len(self._datasources)) + " datasources: " + self.createHeaderString())
        
        mutations = self._inputCreator.createMutations()
        if mutations is None: 
            self.logger.warn("Mutation list points to None after creation.")
            
        mutations = self._annotateMutations(mutations)
        if mutations is None: 
            self.logger.warn("Mutation list points to None after annotation.")
        
        mutations = self._applyManualAnnotations(mutations, self._manualAnnotations)
        if mutations is None: 
            self.logger.warn("Mutation list points to None after manual annotations.")

        comments = self._createComments()
        metadata = self._createMetadata()

        filename = self._outputRenderer.renderMutations(mutations, metadata=metadata, comments=comments)
        return filename
    
    def _applyManualAnnotations(self, mutations, manualAnnotations):
        # TODO: Low priority -- Could speed this up by creating annotations ahead of time.
        manualAnnotationKeys = manualAnnotations.keys()
        for m in mutations:
            for k in manualAnnotationKeys:
                m.createAnnotation(k, manualAnnotations[k], annotationSource="MANUAL")
            yield m

    def _createManualAnnotationsForMetadata(self, manualAnnotations):
        result = {}
        manualAnnotationKeys = manualAnnotations.keys()
        for k in manualAnnotationKeys:
            result[k] = Annotation(manualAnnotations[k], datasourceName="MANUAL")
        return result

    def createHeaderString(self):
        """
        Create a default header string that lists version of Oncotator and datasource information.

        :return: string
        """
        datasourceStrings = []
        for ds in self._datasources:
            datasourceStrings.append(" " + ds.title + " " + ds.version + " ")
        
        return "Oncotator " +  VERSION + "|" + "|".join(datasourceStrings)
    
    def _annotateMutations(self, mutations):
        if len(self._datasources) == 0:
            self.logger.warn("THERE ARE NO DATASOURCES REGISTERED")
        for m in mutations:
            for datasource in self._datasources:
                m = datasource.annotate_mutation(m)
            yield m
    