#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from aws_cdk import core
from confitec.confitec_stack import ConfitecStack


app = core.App()
ConfitecStack(app, "ConfitecStack")

app.synth()
