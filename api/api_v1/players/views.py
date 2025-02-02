from api.api_v1.crud import player_crud
from api.api_v1.players.schemas import PlayerCreate, PlayerRead, PlayerUpdate
from api.api_v1.views import ViewsBase
from core.models.player import Player as PlayerModel

player_views = ViewsBase[
    PlayerModel,
    PlayerCreate,
    PlayerRead,
    PlayerUpdate
](
    model=PlayerModel,
    crud=player_crud,
    read_schema=PlayerRead,
    create_schema=PlayerCreate,
    update_schema=PlayerUpdate,
)
