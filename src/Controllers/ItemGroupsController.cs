using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v2/item_groups")]
public class ItemGroupsController : ControllerBase
{

    private readonly IItemGroupService _itemGroupService;

    public ItemGroupsController(IItemGroupService itemGroupService){
        _itemGroupService = itemGroupService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<ItemGroup>), 200)]
    public async Task<IActionResult> GetItemGroups(){
        IEnumerable<ItemGroup>? itemGroups = await _itemGroupService.GetAll();
        return itemGroups == null ? NotFound() : Ok( itemGroups );
    }

    [HttpGet("{item_group_id}")]
    [ProducesResponseType(typeof(ItemGroup), 200)]
    public async Task<IActionResult> GetItemGroup(int item_group_id){
        ItemGroup? itemGroup = await _itemGroupService.GetItemGroup(item_group_id);
        return itemGroup == null ? NotFound() : Ok( itemGroup );
    }


    [HttpGet("{item_group_id}/items")]
    [ProducesResponseType(typeof(IEnumerable<Item>), 200)]
    public async Task<IActionResult> GetItems(int item_group_id){
        IEnumerable<Item>? items = await _itemGroupService.GetItems(item_group_id);
        return items == null ? NotFound() : Ok( items );
    }


    [HttpPost("")]
    [ProducesResponseType(typeof(ItemGroup), 201)]
    public async Task<IActionResult> AddItemGroup([FromBody] ItemGroup itemGroup){
        ItemGroup? group = await _itemGroupService.AddItemGroup(itemGroup);
        return group == null ? StatusCode(500) : Ok( group );
    }


    [HttpPut("{item_group_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> UpdateItemGroup(int item_group_id, [FromBody] ItemGroup itemGroup){
        await _itemGroupService.UpdateItemGroup(item_group_id, itemGroup);
        return NoContent();
    }


    [HttpDelete("{item_group_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteItemGroup(int item_group_id){
        await _itemGroupService.DeleteItemGroup(item_group_id);
        return NoContent();
    }


}