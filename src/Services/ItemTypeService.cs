using Microsoft.EntityFrameworkCore;

public class ItemTypeService : IItemTypeService
{

    private readonly DataContext _context;

    public ItemTypeService(DataContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<ItemType>?> GetItemTypes()
    {
        return await _context.ItemTypes.ToListAsync();
    }

    public async Task<ItemType?> GetItemType(int itemTypeId)
    {
        return await _context.ItemTypes.FindAsync(itemTypeId);
    }

    public async Task<IEnumerable<Item>?> GetItemsByItemType(int itemTypeId)
    {
        return await _context.Items.Where(i => i.ItemType == itemTypeId).ToListAsync();
    }

    public async Task<ItemType?> CreateItemType(ItemType itemType)
    {
        itemType.CreatedAt = DateTime.UtcNow;
        itemType.UpdatedAt = DateTime.UtcNow;
        _context.ItemTypes.Add(itemType);
        await _context.SaveChangesAsync();
        return itemType;
    }

    public async Task<ItemType?> UpdateItemType(int itemTypeId, ItemType itemType)
    {
        itemType.Id = itemTypeId;
        itemType.UpdatedAt = DateTime.UtcNow;
        _context.ItemTypes.Update(itemType);
        await _context.SaveChangesAsync();
        return itemType;
    }

    public async Task DeleteItemType(int itemTypeId)
    {
        ItemType? itemType = await _context.ItemTypes.FindAsync(itemTypeId);
        if (itemType == null) return;
        _context.ItemTypes.Remove(itemType);
        await _context.SaveChangesAsync();
    }

}

public interface IItemTypeService
{

    Task<IEnumerable<ItemType>?> GetItemTypes();

    Task<ItemType?> GetItemType(int itemTypeId);

    Task<IEnumerable<Item>?> GetItemsByItemType(int itemTypeId);

    Task<ItemType?> CreateItemType(ItemType itemType);

    Task<ItemType?> UpdateItemType(int itemTypeId, ItemType itemType);

    Task DeleteItemType(int itemTypeId);

}
