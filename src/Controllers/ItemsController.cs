using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v2/items")]
public class ItemsController : ControllerBase
{

    private readonly IItemService _itemService;

    public ItemsController(IItemService itemService){
        _itemService = itemService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<Item>), 200)]
    public async Task<IActionResult> GetItems(){
        IEnumerable<Item>? items = await _itemService.GetItems();
        return items == null ? NotFound() : Ok( items );
    }


    [HttpGet("{item_id}")]
    [ProducesResponseType(typeof(Item), 200)]
    public async Task<IActionResult> GetItem(string item_id){
        Item? item = await _itemService.GetItem(item_id);
        return item == null ? NotFound() : Ok( item );
    }


    [HttpGet("{item_id}/inventory")]
    [ProducesResponseType(typeof(IEnumerable<Inventory>), 200)]
    public async Task<IActionResult> GetInventory(string item_id){
        IEnumerable<Inventory>? inventories = await _itemService.GetInventories(item_id);
        return inventories == null ? NotFound() : Ok( inventories );
    }


    [HttpGet("{item_id}/inventory/totals")]
    [ProducesResponseType(typeof(InventoryTotal), 200)]
    public async Task<IActionResult> GetTotals(string item_id){
        InventoryTotal? total = await _itemService.GetTotals(item_id);
        return total == null ? StatusCode(500) : Ok( total );
    }


    [HttpPost("")]
    [ProducesResponseType(typeof(Item), 201)]
    public async Task<IActionResult> AddItem([FromBody] Item item){
        Item? item1 = await _itemService.AddItem(item);
        return item1 == null ? StatusCode(500) : CreatedAtAction(nameof(GetItem), new { item_id = item1.Uid }, item1);
    }

    
    [HttpPut("{item_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> UpdateItem(string item_id, [FromBody] Item item){
        await _itemService.UpdateItem(item_id, item);
        return NoContent();
    }


    [HttpDelete("{item_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteItem(string item_id){
        await _itemService.DeleteItem(item_id);
        return NoContent();
    }

}