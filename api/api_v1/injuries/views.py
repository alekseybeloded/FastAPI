from api.api_v1.crud import injury_crud
from api.api_v1.injuries.schemas import InjuryCreate, InjuryRead, InjuryUpdate
from api.api_v1.views import ViewsBase
from core.models.injury import Injury as InjuryModel

injury_views = ViewsBase[
    InjuryModel,
    InjuryCreate,
    InjuryRead,
    InjuryUpdate,
](
    model=InjuryModel,
    crud=injury_crud,
    read_schema=InjuryRead,
    create_schema=InjuryCreate,
    update_schema=InjuryUpdate,
)
