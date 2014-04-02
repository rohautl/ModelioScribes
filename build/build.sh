#!/bin/sh
THISDIR=`dirname $0`
SRCPROJECTDIR=${THISDIR?}/../../Modelio3Workspace/Systeme/
SRCTEMPLATESPATTERN=${SRCPROJECTDIR}/doc/templates/*.jar
SRCSTYLESPATTERN=${SRCPROJECTDIR}/data/.config/styles/S*.style

OUTDIR=${THISDIR?}/..
OUTTEMPLATEDIR=${OUTDIR?}/templates
OUTSTYLEDIR=${OUTDIR?}/styles

echo "Copying these templates: "
ls ${SRCTEMPLATESPATTERN?}
cp ${SRCTEMPLATESPATTERN?} ${OUTTEMPLATEDIR?}

echo "Copying these styles: "
ls ${SRCSTYLESPATTERN?}
cp ${SRCSTYLESPATTERN?} ${OUTSTYLEDIR?}