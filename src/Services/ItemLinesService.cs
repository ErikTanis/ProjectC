using Microsoft.EntityFrameworkCore;

public class ItemLinesService : IItemLinesService
{

    private readonly DataContext _context;

    public ItemLinesService(DataContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<ItemLine>?> GetItemLines(){
        return await _context.ItemLines.ToListAsync();
    }


    public async Task<ItemLine?> GetItemLine(int item_line_id){
        return await _context.ItemLines.FindAsync(item_line_id);
    }


    public async Task<IEnumerable<Item>?> GetItems(int item_id){
        return await _context.Items.Where(i => i.ItemLine == item_id).ToListAsync();
    }


    public async Task<ItemLine?> CreateItemLine(ItemLine itemLine){
        itemLine.CreatedAt = DateTime.Now;
        itemLine.UpdatedAt = DateTime.Now;
        await _context.ItemLines.AddAsync(itemLine);
        await _context.SaveChangesAsync();
        return itemLine;
    }


    public async Task<ItemLine?> UpdateItemLine(int item_line_id, ItemLine itemLine){
        itemLine.UpdatedAt = DateTime.Now;
        itemLine.Id = item_line_id;
        _context.ItemLines.Update(itemLine);
        await _context.SaveChangesAsync();
        return itemLine;
    }


    public async Task DeleteItemLine(int item_line_id){
        ItemLine? itemLine = await _context.ItemLines.FindAsync(item_line_id);
        if (itemLine == null) return;
        _context.ItemLines.Remove(itemLine);
        await _context.SaveChangesAsync();
    }



}

public interface IItemLinesService
{

    Task<IEnumerable<ItemLine>?> GetItemLines();
    Task<ItemLine?> GetItemLine(int item_line_id);
    Task<IEnumerable<Item>?> GetItems(int item_id);
    Task<ItemLine?> CreateItemLine(ItemLine itemLine);
    Task<ItemLine?> UpdateItemLine(int item_line_id, ItemLine itemLine);
    Task DeleteItemLine(int item_line_id);

}