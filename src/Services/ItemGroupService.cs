using Microsoft.EntityFrameworkCore;

public class ItemGroupService : IItemGroupService
{

    private readonly DataContext _context;

    public ItemGroupService(DataContext context){
        _context = context;
    }

    public async Task<IEnumerable<ItemGroup>?> GetAll(){
        return await _context.ItemGroups.ToListAsync();
    }


    public async Task<ItemGroup?> GetItemGroup(int ItemGroupId){
        return await _context.ItemGroups.FindAsync(ItemGroupId);
    }


    public async Task<IEnumerable<Item>?> GetItems(int ItemGroupId){
        return await _context.Items.Where(item => item.ItemGroup == ItemGroupId).ToListAsync();   
    }


    public async Task<ItemGroup?> AddItemGroup(ItemGroup itemGroup){
        itemGroup.CreatedAt = DateTime.Now;
        itemGroup.UpdatedAt = DateTime.Now;
        await _context.ItemGroups.AddAsync(itemGroup);
        return await GetItemGroup(itemGroup.Id);
    }


    public async Task UpdateItemGroup(int ItemGroupId, ItemGroup itemGroup){
        itemGroup.Id = ItemGroupId;
        itemGroup.UpdatedAt = DateTime.Now;
        _context.ItemGroups.Update(itemGroup);
        await _context.SaveChangesAsync();
    }


    public async Task DeleteItemGroup(int ItemGroupId){
        ItemGroup? itemGroup = await _context.ItemGroups.FindAsync(ItemGroupId);
        if(itemGroup == null) return;
        _context.ItemGroups.Remove(itemGroup);
        await _context.SaveChangesAsync();
    }



}

public interface IItemGroupService
{

    Task<IEnumerable<ItemGroup>?> GetAll();
    Task<ItemGroup?> GetItemGroup(int ItemGroupId);
    Task<IEnumerable<Item>?> GetItems(int ItemGroupId);
    Task<ItemGroup?> AddItemGroup(ItemGroup itemGroup);
    Task UpdateItemGroup(int ItemGroupId, ItemGroup itemGroup);
    Task DeleteItemGroup(int ItemGroupId);

}