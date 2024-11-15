using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/v2/item_lines")]
public class ItemLinesController : ControllerBase
{
    private readonly IItemLinesService _itemLinesService;

    public ItemLinesController(IItemLinesService itemLinesService)
    {
        _itemLinesService = itemLinesService;
    }

    [HttpGet("")]
    [ProducesResponseType(typeof(IEnumerable<ItemLine>), 200)]
    public async Task<IActionResult> GetItemLines()
    {
        IEnumerable<ItemLine>? itemLines = await _itemLinesService.GetItemLines();
        return itemLines == null ? NotFound() : Ok( itemLines );
    }

    [HttpGet("{item_line_id}")]
    [ProducesResponseType(typeof(ItemLine), 200)]
    public async Task<IActionResult> GetItemLine(int item_line_id)
    {
        ItemLine? itemLine = await _itemLinesService.GetItemLine(item_line_id);
        return itemLine == null ? NotFound() : Ok( itemLine );
    }

    [HttpGet("{item_id}/items")]
    [ProducesResponseType(typeof(IEnumerable<Item>), 200)]
    public async Task<IActionResult> GetItems(int item_id)
    {
        IEnumerable<Item>? items = await _itemLinesService.GetItems(item_id);
        return items == null ? NotFound() : Ok( items );
    }

    [HttpPost("")]
    [ProducesResponseType(typeof(ItemLine), 201)]
    public async Task<IActionResult> CreateItemLine(ItemLine itemLine)
    {
        ItemLine? createdItemLine = await _itemLinesService.CreateItemLine(itemLine);
        return createdItemLine == null ? BadRequest() : CreatedAtAction(nameof(GetItemLine), new { item_line_id = createdItemLine.Id }, createdItemLine);
    }

    [HttpPut("{item_line_id}")]
    [ProducesResponseType(typeof(ItemLine), 200)]
    public async Task<IActionResult> UpdateItemLine(int item_line_id, ItemLine itemLine)
    {
        ItemLine? updatedItemLine = await _itemLinesService.UpdateItemLine(item_line_id, itemLine);
        return updatedItemLine == null ? NotFound() : Ok( updatedItemLine );
    }

    [HttpDelete("{item_line_id}")]
    [ProducesResponseType(204)]
    public async Task<IActionResult> DeleteItemLine(int item_line_id)
    {
        await _itemLinesService.DeleteItemLine(item_line_id);
        return NoContent();
    }

}