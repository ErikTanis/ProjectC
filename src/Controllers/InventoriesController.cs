using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v2/inventories")]
public class InventoriesController : ControllerBase
{

    private readonly IInventoryService _inventoryService;

    public InventoriesController(IInventoryService inventoryService){
        _inventoryService = inventoryService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<Inventory>), 200)]
    public async Task<IActionResult> GetInventories(){
        IEnumerable<Inventory>? inventories = await _inventoryService.GetInventories();
        return inventories == null ? NotFound() : Ok( inventories );
    }


    [HttpGet("{inventory_id}")]
    [ProducesResponseType(typeof(Inventory), 200)]
    public async Task<IActionResult> GetInventory(int inventory_id){
        Inventory? inventory = await _inventoryService.GetInventory(inventory_id);
        return inventory == null ? NotFound() : Ok( inventory );
    }


    [HttpPost("")]
    [ProducesResponseType(typeof(Inventory), 201)]
    public async Task<IActionResult> AddInventory([FromBody] Inventory inventory){
        Inventory? inventory1 = await _inventoryService.AddInventory(inventory);
        return inventory1 == null ? StatusCode(500) : CreatedAtAction(nameof(GetInventory), new { inventory_id = inventory1.Id }, inventory1);
    }


    [HttpPut("{inventory_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> UpdateInventory(int inventory_id, [FromBody] Inventory inventory){
        await _inventoryService.UpdateInventory(inventory_id, inventory);
        return NoContent();
    }


    [HttpDelete("{inventory_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteInventory(int inventory_id){
        await _inventoryService.DeleteInventory(inventory_id);
        return NoContent();
    }

}