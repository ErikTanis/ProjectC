using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v2/item_types")]
public class ItemTypesController : ControllerBase
{
    private readonly IItemTypeService _itemTypeService;

    public ItemTypesController(IItemTypeService itemTypeService)
    {
        _itemTypeService = itemTypeService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<ItemType>), 200)]
    public async Task<IActionResult> GetItemTypes()
    {
        IEnumerable<ItemType>? itemTypes = await _itemTypeService.GetItemTypes();
        return itemTypes == null ? NotFound() : Ok( itemTypes );
    }

    [HttpGet("{item_type_id}")]
    [ProducesResponseType(typeof(ItemType), 200)]
    public async Task<IActionResult> GetItemType(int itemTypeId)
    {
        ItemType? itemType = await _itemTypeService.GetItemType(itemTypeId);
        return itemType == null ? NotFound() : Ok( itemType );
    }

    [HttpGet("{item_type_id}/items")]
    [ProducesResponseType(typeof(IEnumerable<Item>), 200)]
    public async Task<IActionResult> GetItemsByItemType(int itemTypeId)
    {
        IEnumerable<Item>? items = await _itemTypeService.GetItemsByItemType(itemTypeId);
        return items == null ? NotFound() : Ok( items );
    }

    [HttpPost("")]
    [ProducesResponseType(typeof(ItemType), 201)]
    public async Task<IActionResult> CreateItemType([FromBody] ItemType itemType)
    {
        ItemType? createdItemType = await _itemTypeService.CreateItemType(itemType);
        return createdItemType == null ? StatusCode(500) : CreatedAtAction(nameof(GetItemType), new { itemTypeId = createdItemType.Id }, createdItemType);
    }

    [HttpPut("{item_type_id}")]
    [ProducesResponseType(typeof(ItemType), 200)]
    public async Task<IActionResult> UpdateItemType(int itemTypeId, [FromBody] ItemType itemType)
    {
        ItemType? updatedItemType = await _itemTypeService.UpdateItemType(itemTypeId, itemType);
        return updatedItemType == null ? NotFound() : Ok( updatedItemType );
    }

    [HttpDelete("{item_type_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteItemType(int itemTypeId)
    {
        await _itemTypeService.DeleteItemType(itemTypeId);
        return NoContent();
    }

}