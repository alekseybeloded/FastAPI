from api.api_v1.crud import team_crud
from api.api_v1.teams.schemas import TeamCreate, TeamRead, TeamUpdate
from api.api_v1.views import ViewsBase
from core.models.team import Team as TeamModel

team_views = ViewsBase[
    TeamModel,
    TeamCreate,
    TeamRead,
    TeamUpdate,
](
    model=TeamModel,
    crud=team_crud,
    read_schema=TeamRead,
    create_schema=TeamCreate,
    update_schema=TeamUpdate,
)
