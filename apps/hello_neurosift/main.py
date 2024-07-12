from pairio.sdk import App
from UnitsSummary1 import UnitsSummary1
from EphysSummary1 import EphysSummary1
from AviToMp4 import AviToMp4Processor

app = App(
    app_name='hello_neurosift',
    description='Neurosift processors'
)

app.add_processor(UnitsSummary1)
app.add_processor(EphysSummary1)
app.add_processor(AviToMp4Processor)

if __name__ == '__main__':
    app.run()
